import subprocess
import sys

class CodeAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def analyze_python(self):
        result = subprocess.run(['flake8', self.file_path], capture_output=True, text=True)
        return result.stdout

    # 同様に他の言語もメソッドを追加

if __name__ == "__main__":
    file_path = sys.argv[1]  # コマンドライン引数からファイルパスを取得
    analyzer = CodeAnalyzer(file_path)
    print(analyzer.analyze_python())