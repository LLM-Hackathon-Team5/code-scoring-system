<?php
require 'vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$API_URL = $_ENV['PALM_API_URL'];  // Get PaLM 2 API URL from environment variable

function generateComment($analysisResults) {
    if (empty($analysisResults)) {
        return "問題は見つかりませんでした。良い仕事をしました！";
    }

    $text = implode('. ', array_column($analysisResults, 'description'));
    $response = file_get_contents($API_URL, false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => 'Content-type: application/json',
            'content' => json_encode(['text' => $text]),
        ],
    ]));
    $comment = json_decode($response, true)['comment'];

    return "### PHPコードレビュー\n\n以下の問題を修正してください:\n\n$comment";
}

// Example usage
$analysisResults = [
    ['description' => 'This is an issue.'],
    // Add more issues here
];
echo generateComment($analysisResults);