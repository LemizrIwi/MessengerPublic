from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

# Flask Setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # für Session-Sicherheit

# SocketIO Setup
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Chat-Nachrichten empfangen und an alle senden
@socketio.on('message')
def handle_message(msg):
    print(f"Nachricht: {msg}")
    send(msg, broadcast=True)

# einfache Startseite (optional)
@app.route('/')
def index():
    return "Messenger Server läuft. Verbinde dich über SocketIO-Client."

# Render gibt den Port über Umgebungsvariable vor
port = int(os.environ.get('PORT', 5000))

if __name__ == "__main__":
    # host 0.0.0.0, damit Render den Server erreichen kann
    socketio.run(app, host='0.0.0.0', port=port)
