import os
import requests

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # GitHubのトークンを環境変数から取得

def post_comment(issue_url, comment_body):
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',  # GitHubのトークンをヘッダーにセット
        'Accept': 'application/vnd.github.v3+json',  # GitHub API v3のヘッダー
    }
    data = {
        'body': comment_body,  # コメントの内容
    }
    response = requests.post(issue_url, headers=headers, json=data)  # POSTリクエストを送信
    response.raise_for_status()  # エラーレスポンスが返された場合は例外を発生させる

# サンプルのコメント内容とPull RequestのURL
sample_comment = "これはテストコメントです。"
pr_url = "https://api.github.com/repos/user/repo/issues/1/comments"  # 実際のURLに置き換える

post_comment(pr_url, sample_comment)  # コメントを投稿