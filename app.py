from flask import Flask, jsonify


app = Flask(__name__)

# /health route
@app.route('/health')
def health():
    return jsonify({"status": "ok"})

# /version route
@app.route('/version')
def version():
    return jsonify({
        "version": "1.2.14",
        "nextUpdate": "June 17, 2026"
    })

# /status route
@app.route('/status')
def status():
    return jsonify({
        "status":       "operational",
        "services": {
            "vercel":       "ok",
            "supabase":     "ok",
            "twilio":       "ok"
        }
        
    })
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)