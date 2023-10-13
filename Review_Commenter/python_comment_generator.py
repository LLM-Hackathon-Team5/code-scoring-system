import json
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

API_URL = os.getenv('PALM_API_URL')  # Get PaLM 2 API URL from environment variable

def generate_comment(analysis_results):
    if not analysis_results:
        return "問題は見つかりませんでした。良い仕事をしました！"
    
    issues = [issue['description'] for issue in analysis_results]
    text = '. '.join(issues)
    response = requests.post(API_URL, json={'text': text})
    comment = response.json()['comment']
    
    return f"### Pythonコードレビュー\n\n以下の問題を修正してください:\n\n{comment}"

# Example usage
if __name__ == "__main__":
    with open('python_analysis_results.json', 'r') as file:
        analysis_results = json.load(file)
    
    comment = generate_comment(analysis_results)
    print(comment)