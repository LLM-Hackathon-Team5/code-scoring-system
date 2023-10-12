import subprocess
import sys

class PHPAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def analyze(self):
        result = subprocess.run(['phpcs', self.file_path], capture_output=True, text=True)
        return result.stdout

if __name__ == "__main__":
    file_path = sys.argv[1]
    analyzer = PHPAnalyzer(file_path)
    print(analyzer.analyze())