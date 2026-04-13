from flask import Flask
import os

app = Flask(__name__)

# Read from environment variables — change per release
RELEASE = os.environ.get("RELEASE", "1")
COLOR = os.environ.get("COLOR", "blue")
BG_COLORS = {
    "blue": "#1a73e8",
    "green": "#34a853",
    "red": "#ea4335",
    "purple": "#9c27b0"
}
BG_COLOR = BG_COLORS.get(COLOR, "#1a73e8")

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>MyApp Release {RELEASE}</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                background-color: {BG_COLOR};
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-family: 'Segoe UI', sans-serif;
                color: white;
            }}
            .card {{
                background: rgba(255,255,255,0.15);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 60px 80px;
                text-align: center;
                box-shadow: 0 8px 32px rgba(0,0,0,0.2);
                border: 1px solid rgba(255,255,255,0.3);
            }}
            .release {{ font-size: 90px; font-weight: 900; }}
            .label  {{ font-size: 22px; opacity: 0.85; margin-bottom: 10px; }}
            .color-badge {{
                display: inline-block;
                background: rgba(255,255,255,0.25);
                padding: 6px 20px;
                border-radius: 20px;
                font-size: 16px;
                margin-top: 15px;
                text-transform: uppercase;
                letter-spacing: 2px;
            }}
            .hostname {{
                font-size: 13px;
                opacity: 0.6;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="label">MyApp — Kubernetes Practice</div>
            <div class="release">v{RELEASE}</div>
            <div class="color-badge">🎨 {COLOR}</div>
            <div class="hostname">Pod: {os.environ.get("HOSTNAME", "unknown")}</div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {{"status": "ok", "release": RELEASE, "color": COLOR}}

@app.route("/version")
def version():
    return {{"release": RELEASE, "color": COLOR}}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
