import subprocess
import sys
import json
import os
import requests
from dotenv import load_dotenv

# .envファイルから環境変数をロード
load_dotenv()

# 環境変数からPaLM 2の基本URLとモデルのパスを取得して、完全なAPI URLを構築
PALM2_BASE_URL = os.getenv('PALM2_BASE_URL')
PALM2_MODEL_PATH = os.getenv('PALM2_MODEL_PATH')
API_URL = f"{PALM2_BASE_URL}{PALM2_MODEL_PATH}"  

class PythonAnalyzer:
    def __init__(self, file_path, dev_rules_jsonl):
        self.file_path = file_path
        self.dev_rules = self._load_dev_rules(dev_rules_jsonl)

    def _load_dev_rules(self, dev_rules_jsonl):
        with open(dev_rules_jsonl, 'r') as file:
            return [json.loads(line) for line in file]

    def analyze(self):
        result = subprocess.run(['flake8', self.file_path], capture_output=True, text=True)
        issues = result.stdout.strip().split('\n') if result.stdout else []
        detailed_issues = [self._get_detailed_issue(issue) for issue in issues]
        return detailed_issues

    def _get_detailed_issue(self, issue):
        # PaLM 2からコメントを取得
        response = requests.post(API_URL, json={'text': issue})
        palm2_comment = response.json()['comment']

        # 開発ルールに基づいてルールベースのコメントを取得
        rule_based_comment = self._get_rule_based_comment(issue)

        return {
            'issue': issue,
            'palm2_comment': palm2_comment,
            'rule_based_comment': rule_based_comment
        }

    def _get_rule_based_comment(self, issue):
        # ここで、読み込んだ開発ルールと問題を照合して、適切なコメントを返します
        # 実際の実装は、開発ルールと問題の構造に依存します
        for rule in self.dev_rules:
            if self._issue_matches_rule(issue, rule):
                return rule['output_text']  # 例です、実際のルール構造に基づいて調整してください

        return "該当するルールベースのコメントは見つかりませんでした。"

    def _issue_matches_rule(self, issue, rule):
        # 与えられた問題が与えられたルールと一致するかどうかを判断するメソッドを実装します
        # これはプレースホルダであり、実際の実装に置き換える必要があります
        return issue in rule['input_text']  # 例です、実際のルール構造に基づいて調整してください

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python_analyzer.py <file_path> <dev_rules_jsonl>")
        sys.exit(1)

    file_path = sys.argv[1]
    dev_rules_jsonl = sys.argv[2]  # 開発ルールのJSONLファイルのパスをここに渡します

    analyzer = PythonAnalyzer(file_path, dev_rules_jsonl)
    analysis_results = analyzer.analyze()
    print(json.dumps(analysis_results, indent=2))