import sys
from github import Github

class ReviewCommenter:
    def __init__(self, token, repo_name, pull_number):
        self.github = Github(token)
        self.repo = self.github.get_repo(repo_name)
        self.pull = self.repo.get_pull(pull_number)

    def post_comment(self, message):
        self.pull.create_issue_comment(message)

if __name__ == "__main__":
    token = sys.argv[1]  # GitHubのトークン
    repo_name = sys.argv[2]  # リポジトリ名
    pull_number = int(sys.argv[3])  # プルリクエスト番号
    message = sys.argv[4]  # コメントのメッセージ

    commenter = ReviewCommenter(token, repo_name, pull_number)
    commenter.post_comment(message)