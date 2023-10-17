import json
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 環境変数からPaLM 2の基本URLとモデルのパスを取得して、完全なAPI URLを構築
PALM2_BASE_URL = os.getenv('PALM2_BASE_URL')
PALM2_MODEL_PATH = os.getenv('PALM2_MODEL_PATH')
API_URL = f"{PALM2_BASE_URL}{PALM2_MODEL_PATH}"  

def generate_comment(analysis_results):
    if not analysis_results:
        return "問題は見つかりませんでした。良い仕事をしました！"

    issues = [issue['detailed_comment'] for issue in analysis_results]  # PaLM 2から取得した詳細コメントを使用
    text = '. '.join(issues)
    response = requests.post(API_URL, json={'text': text})  # PaLM 2に解析結果を送信してレビューコメントを生成
    comment = response.json()['comment']

    return f"### Pythonコードレビュー\n\n以下の問題を修正してください:\n\n{comment}"

if __name__ == "__main__":
    with open('python_analysis_results.json', 'r') as file:
        analysis_results = json.load(file)  # 解析結果をファイルからロード

    comment = generate_comment(analysis_results)  # 解析結果に基づいてレビューコメントを生成
    print(comment)