from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.post("/run")
def run_code():
    code = request.json.get("code", "")

    result = subprocess.run(
        ["docker", "run", "--rm", "-i", "python-science"],
        input=code,
        text=True,
        capture_output=True
    )

    raw = result.stdout

    # Parser robusto
    output = ""
    image = ""

    if "<<OUTPUT>>" in raw:
        output = raw.split("<<OUTPUT>>")[1].split("<<IMAGE>>")[0]
        output = output.replace("\\n", "\n").strip()

    if "<<IMAGE>>" in raw:
        image = raw.split("<<IMAGE>>")[1].strip()

    return jsonify({
        "output": output,
        "image": image
    })

if __name__ == "__main__":
    app.run(debug=True)
