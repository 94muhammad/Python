from flask import Flask, request, jsonify
import openai

openai.api_key = "your-api-key"

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def gen_text():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if not prompt:
            return jsonify({"error": "Prompt is required."}), 400

        try:
            response = openai.Completion.create(
                engine="text-davinci-001",
                prompt=prompt,
                max_tokens=60,
                n=1,
                stop=None,
                temperature=0.7,
            )

            return jsonify({"text": response.choices[0].text.strip()})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return """
    <form method="POST" action="/">
        <label for="prompt">Enter a prompt:</label>
        <input type="text" name="prompt" id="prompt">
        <button type="submit">Generate Text</button>
    </form>
    """
if __name__ == ('__main__'):
    app.run(debug=True)

