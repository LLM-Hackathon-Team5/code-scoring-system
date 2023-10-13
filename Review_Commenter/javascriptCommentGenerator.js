require('dotenv').config();
const fetch = require('node-fetch');

const API_URL = process.env.PALM_API_URL;  // Get PaLM 2 API URL from environment variable

const generateComment = async (analysisResults) => {
    if (!analysisResults.length) {
        return "問題は見つかりませんでした。良い仕事をしました！";
    }

    const text = analysisResults.map(issue => issue.description).join('. ');
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
    });
    const { comment } = await response.json();

    return `### JavaScriptコードレビュー\n\n以下の問題を修正してください:\n\n${comment}`;
}

// Example usage
const analysisResults = [
    { description: "This is an issue." },
    // Add more issues here
];
generateComment(analysisResults).then(console.log);