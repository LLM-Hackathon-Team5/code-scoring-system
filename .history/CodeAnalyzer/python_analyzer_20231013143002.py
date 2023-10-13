import subprocess
import sys
import json
import os
import requests
from dotenv import load_dotenv
from dev_rules_loader import DevRulesLoader  # ユーザーの開発ルールをロードするモジュール

# Load environment variables from .env file
load_dotenv()

API_URL = os.getenv('Tuned_PALM2_API_URL')  # PaLM 2のAPI URLを環境変数から取得

class PythonAnalyzer:
    def __init__(self, file_path, dev_rules):
        self.file_path = file_path
        self.dev_rules = dev_rules  # ユーザーの開発ルールをインスタンス変数として保持

    def analyze(self):
        result = subprocess.run(['flake8', self.file_path], capture_output=True, text=True)  # flake8でPythonコードを解析
        issues = result.stdout.strip().split('\n') if result.stdout else []
        detailed_issues = [self._get_detailed_issue(issue) for issue in issues]
        return detailed_issues

    def _get_detailed_issue(self, issue):
        response = requests.post(API_URL, json={'text': issue})  # PaLM 2に解析結果を送信して詳細なコメントを取得
        comment = response.json()['comment']
        return {
            'issue': issue,
            'detailed_comment': comment,
            'rule_based_comment': self._get_rule_based_comment(issue)  # ユーザーの開発ルールに基づいてコメントを生成
        }

    def _get_rule_based_comment(self, issue):
        # Here map the issue to a specific rule in self.dev_rules and return the rule-based comment
        # This implementation will depend on the structure of your dev_rules and issues
        return "This is a rule-based comment."

if __name__ == "__main__":
    file_path = sys.argv[1]
    rules_file_path = sys.argv[2]

    loader = DevRulesLoader(rules_file_path)
    dev_rules = loader.load_rules()  # ユーザーの開発ルールをファイルからロード

    analyzer = PythonAnalyzer(file_path, dev_rules)
    analysis_results = analyzer.analyze()
    print(json.dumps(analysis_results, indent=2))