from flask import Flask, request, jsonify
import re

app = Flask(__name__)

CC_RE = re.compile(r"^\d{15,16}\|\d{2}\|\d{2,4}\|\d{3,4}$")

@app.route("/", methods=["GET"])
@app.route("/shopify-checker", methods=["GET"])
def checker():
    cc = request.args.get("cc", "").strip()
    site = request.args.get("url", "").strip()
    proxy = request.args.get("proxy", "").strip()

    if not site:
        return jsonify({
            "Status": "Error",
            "Response": "Missing site param",
            "Gate": "shopiii",
            "Price": "-"
        })

    if not cc:
        return jsonify({
            "Status": "Error",
            "Response": "No CC provided",
            "Gate": "shopiii",
            "Price": "-"
        })

    if not CC_RE.match(cc):
        return jsonify({
            "Status": "Dead",
            "Response": "Invalid card format",
            "Gate": "shopiii",
            "Price": "-"
        })

    card, month, year, cvv = cc.split("|")

    # SAFE TEST MODE RESPONSES
    if card == "4242424242424242":
        status = "Approved"
        response = "Approved test card"
    elif card == "4000000000009995":
        status = "Approved"
        response = "Insufficient funds test card"
    elif card == "4000000000000002":
        status = "Dead"
        response = "Card declined test card"
    else:
        status = "Dead"
        response = "Test mode only. Real card checking disabled."

    return jsonify({
        "Status": status,
        "Response": response,
        "Gate": "shopiii",
        "Price": "-",
        "cc": cc,
        "site": site,
        "proxy": "provided" if proxy else "none"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
