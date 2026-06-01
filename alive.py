from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health_check():
    # Returns a 200 OK status code to tell Koyeb the container is healthy
    return "OK", 200

if __name__ == "__main__":
    # Koyeb automatically assigns a PORT variable, defaults to 8000
    port = int(os.environ.get("PORT", 8000))
    # Must bind to 0.0.0.0 so it listens to external requests from Koyeb
    app.run(host="0.0.0.0", port=port)
