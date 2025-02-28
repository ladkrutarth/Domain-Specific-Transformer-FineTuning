
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the text-generation model
scouting_report_pipeline = pipeline('text-generation', model='gpt2')

@app.route('/generate', methods=['POST'])
def generate_report():
    try:
        data = request.get_json()
        if not data or "player_data" not in data:
            return jsonify({"error": "Invalid input"}), 400

        player_data = data["player_data"]
        report = scouting_report_pipeline(player_data, max_length=150, num_return_sequences=1)
        return jsonify({"Generated NFL Scouting Report": report[0]['generated_text']})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error message

if __name__ == '__main__':
    # Run Flask without reloader in development environments
    app.run(host="127.0.0.1", port=5000, debug=False)


