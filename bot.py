from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def checker():

    full_query = request.query_string.decode()

    parts = full_query.split("&url=")

    cc = parts[0] if len(parts) > 0 else ""

    url = ""

    if len(parts) > 1:

        remaining = parts[1]

        if "&proxy=" in remaining:
            url = remaining.split("&proxy=")[0]
        else:
            url = remaining

    # SAME AS OLD API
    if not url:
        return jsonify({
            "status": "Error",
            "message": "Missing site param",
            "error_code": "SITE DEAD"
        })

    if not cc:
        return jsonify({
            "status": "Error",
            "message": "No CC provided",
            "error_code": "NO_CC"
        })

    return jsonify({
        "status": "Live",
        "message": "Checker working",
        "cc": cc,
        "site": url,
        "gateway": "Shopify"
    })

app.run(host="0.0.0.0", port=5000)
