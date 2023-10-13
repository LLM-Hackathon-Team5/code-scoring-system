import subprocess
import sys

class PHPFixer:
    def __init__(self, file_path):
        self.file_path = file_path

    def auto_fix(self):
        result = subprocess.run(['phpcbf', self.file_path], capture_output=True, text=True)
        return result.stdout

if __name__ == "__main__":
    file_path = sys.argv[1]
    fixer = PHPFixer(file_path)
    print(fixer.auto_fix())