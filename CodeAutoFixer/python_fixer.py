import subprocess
import sys

class PythonFixer:
    def __init__(self, file_path):
        self.file_path = file_path

    def auto_fix(self):
        result = subprocess.run(['black', self.file_path], capture_output=True, text=True)
        return result.stdout

if __name__ == "__main__":
    file_path = sys.argv[1]
    fixer = PythonFixer(file_path)
    print(fixer.auto_fix())