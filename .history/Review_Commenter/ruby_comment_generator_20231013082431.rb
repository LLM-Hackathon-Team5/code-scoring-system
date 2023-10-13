require 'json'
require 'net/http'
require 'dotenv'

# Load environment variables from .env file
Dotenv.load

API_URL = URI(ENV['PALM_API_URL'])  # Get PaLM 2 API URL from environment variable

def generate_comment(analysis_results)
    return "問題は見つかりませんでした。良い仕事をしました！" if analysis_results.empty?

    text = analysis_results.map { |issue| issue['description'] }.join('. ')
    response = Net::HTTP.post(
        API_URL,
        { text: text }.to_json,
        { "Content-Type" => "application/json" }
    )
    comment = JSON.parse(response.body)['comment']

    "### Rubyコードレビュー\n\n以下の問題を修正してください:\n\n#{comment}"
end

# Example usage
if __FILE__ == $0
    file = File.read('ruby_analysis_results.json')
    analysis_results = JSON.parse(file)

    comment = generate_comment(analysis_results)
    puts comment
end