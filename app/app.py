from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "Welcome to Jenkins AWS DevOps CI/CD!",
        "version": "1.0.0"
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200
