from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "SHOPIFY CHECKER API ONLINE"

@app.route('/shopify-checker', methods=['GET', 'POST'])
def checker():

    cc = request.args.get("cc")
    url = request.args.get("url")

    if not cc:
        return jsonify({
            "status": "Error",
            "message": "No CC provided",
            "error_code": "NO_CC"
        })

    if not url:
        return jsonify({
            "status": "Error",
            "message": "Missing site param",
            "error_code": "SITE DEAD"
        })

    return jsonify({
        "status": "LIVE",
        "cc": cc,
        "site": url,
        "gateway": "Shopify",
        "message": "Checker working successfully"
    })

app.run(host="0.0.0.0", port=5000)
