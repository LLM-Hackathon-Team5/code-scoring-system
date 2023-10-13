import java.io.*;
import java.net.*;
import java.util.*;
import org.json.*;

public class JavaCommentGenerator {

    private static String API_URL;

    static {
        // 環境変数からPaLM 2 API URLを取得
        API_URL = System.getenv("PALM_API_URL");
    }

    public static String generateComment(String analysisResults) throws Exception {
        if (analysisResults == null || analysisResults.isEmpty()) {
            return "問題は見つかりませんでした。良い仕事をしました！";
        }

        URL url = new URL(API_URL);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type", "application/json; utf-8");

        JSONObject jsonInputString = new JSONObject();
        jsonInputString.put("text", analysisResults);

        try(OutputStream os = con.getOutputStream()) {
            byte[] input = jsonInputString.toString().getBytes("utf-8");
            os.write(input, 0, input.length);
        }

        int code = con.getResponseCode();
        if (code != 200) {
            return "エラーが発生しました";
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
        StringBuilder response = new StringBuilder();
        String responseLine = null;
        while ((responseLine = br.readLine()) != null) {
            response.append(responseLine.trim());
        }

        JSONObject jsonResponse = new JSONObject(response.toString());
        return "### Javaコードレビュー\n\n以下の問題を修正してください:\n\n" + jsonResponse.getString("comment");
    }

    public static void main(String[] args) throws Exception {
        String analysisResults = "コードの説明が不足しています。";  // これは例です
        String comment = generateComment(analysisResults);
        System.out.println(comment);
    }
}