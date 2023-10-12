import subprocess
import sys

class CodeAutoFixer:
    def __init__(self, file_path):
        self.file_path = file_path

    def auto_fix_python(self):
        subprocess.run(['black', self.file_path])
        print(f"{self.file_path} has been auto-fixed.")

    # 同様に他の言語もメソッドを追加

if __name__ == "__main__":
    file_path = sys.argv[1]  # コマンドライン引数からファイルパスを取得
    fixer = CodeAutoFixer(file_path)
    fixer.auto_fix_python()
