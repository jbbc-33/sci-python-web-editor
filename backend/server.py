from flask import Flask, request, jsonify
import subprocess
import base64
import os

app = Flask(__name__)

@app.post("/run")
def run_code():
    code = request.json["code"]

    # Ejecutar run.py con el código del usuario
    process = subprocess.Popen(
        ["python", "run.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(code)

    # Si run.py genera una imagen, la guardará como output.png
    image_data = ""
    if os.path.exists("output.png"):
        with open("output.png", "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
        os.remove("output.png")

    return jsonify({
        "output": stdout + ("\n" + stderr if stderr else ""),
        "image": image_data
    })

app.run(host="0.0.0.0", port=5000)
