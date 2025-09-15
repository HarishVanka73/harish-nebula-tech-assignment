from flask import Flask, jsonify

app = Flask(_name_)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
