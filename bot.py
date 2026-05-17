from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "SHOPIFY CHECKER API ONLINE"

@app.route('/shopify-checker', methods=['GET', 'POST'])
def checker():

    cc = request.args.get("cc")

    if not cc:
        return jsonify({
            "status": "error",
            "message": "No CC provided"
        })

    return jsonify({
        "status": "LIVE",
        "cc": cc,
        "gateway": "Shopify",
        "message": "Checker working successfully"
    })

app.run(host="0.0.0.0", port=5000)
