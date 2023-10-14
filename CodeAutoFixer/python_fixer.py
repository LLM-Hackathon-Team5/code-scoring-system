import subprocess
import sys
import os
import requests
from dotenv import load_dotenv
from dev_rules_loader import DevRulesLoader  # ユーザーの開発ルールをロードするモジュール

# Load environment variables from .env file
load_dotenv()

# 環境変数からPaLM 2の基本URLとモデルのパスを取得して、完全なAPI URLを構築
PALM2_BASE_URL = os.getenv('PALM2_BASE_URL')
PALM2_MODEL_PATH = os.getenv('PALM2_MODEL_PATH')
API_URL = f"{PALM2_BASE_URL}{PALM2_MODEL_PATH}"  

class PythonFixer:
    def __init__(self, file_path, dev_rules):
        self.file_path = file_path
        self.dev_rules = dev_rules  # ユーザーの開発ルールをインスタンス変数として保持

    def auto_fix(self):
        result = subprocess.run(['black', self.file_path], capture_output=True, text=True)  # blackでPythonコードを自動修正
        fixed_code = result.stdout if result.stdout else "No fixes needed."

        response = requests.post(API_URL, json={'text': fixed_code})  # PaLM 2に修正後のコードを送信してコメントを取得
        comment = response.json()['comment']

        return {
            'fixed_code': fixed_code,
            'fix_comment': comment,
            'rule_based_fix': self._get_rule_based_fix(fixed_code)  # ユーザーの開発ルールに基づいて修正コメントを生成
        }

    def _get_rule_based_fix(self, fixed_code):
        # Implement rule-based fixes based on dev_rules
        # This is a placeholder and should be implemented based on the actual rules and issues
        return "This is a rule-based fix comment."

if __name__ == "__main__":
    file_path = sys.argv[1]
    rules_file_path = sys.argv[2]

    loader = DevRulesLoader(rules_file_path)
    dev_rules = loader.load_rules()  # ユーザーの開発ルールをファイルからロード

    fixer = PythonFixer(file_path, dev_rules)
    fix_results = fixer.auto_fix()
    print(fix_results)