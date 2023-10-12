import subprocess
import sys

class PythonAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def analyze(self):
        result = subprocess.run(['flake8', self.file_path], capture_output=True, text=True)
        return result.stdout

if __name__ == "__main__":
    file_path = sys.argv[1]
    analyzer = PythonAnalyzer(file_path)
    print(analyzer.analyze())