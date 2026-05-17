from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def checker():

    full_query = request.query_string.decode()

    parts = full_query.split("&url=")

    cc = parts[0] if len(parts) > 0 else ""

    url = ""
    proxy = ""

    if len(parts) > 1:

        remaining = parts[1]

        if "&proxy=" in remaining:
            url, proxy = remaining.split("&proxy=", 1)
        else:
            url = remaining

    if not cc:
        return jsonify({
            "status": "Error",
            "message": "No CC provided",
            "error_code": "NO_CC"
        })

    return jsonify({
        "status": "LIVE",
        "cc": cc,
        "site": url,
        "proxy": proxy,
        "gateway": "Shopify",
        "message": "Checker working successfully"
    })

app.run(host="0.0.0.0", port=5000)
