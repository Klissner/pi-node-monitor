import os
import requests
from flask import Flask, render_template, jsonify, request, session

# GLOBALE VERSION
monitorversion = "Pi-Network Monitor Beta: 0.01"

# Dynamische Konfiguration aus deiner .env Datei via Docker-Umgebungsvariablen
DEFAULT_NODE_IP = os.environ.get('NODE_IP', '127.0.0.1')
DEFAULT_NODE_PORT = os.environ.get('NODE_PORT', '11626')
DEFAULT_REFRESH = int(os.environ.get('MONITOR_REFRESH', 5))

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_node_status(ip, port):
    """Fragt die lokalen Core-Metriken der Node ab"""
    try:
        url = f"http://{ip}:{port}/info"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return {"online": True, "raw": response.json()}
    except Exception:
        pass
    return {"online": False, "raw": None}

@app.route('/')
def index():
    # Holt Einstellungen aus der Session oder nutzt die .env Defaults
    node_ip = session.get('node_ip', DEFAULT_NODE_IP)
    node_port = session.get('node_port', DEFAULT_NODE_PORT)
    refresh = session.get('refresh', DEFAULT_REFRESH)
    current_lang = request.args.get('lang', session.get('lang', 'de'))
    session['lang'] = current_lang

    return render_template('index.html', 
                           node_ip=node_ip, 
                           node_port=node_port, 
                           refresh=refresh, 
                           current_lang=current_lang,
                           monitorversion=monitorversion)

@app.route('/api/data')
def api_data():
    node_ip = session.get('node_ip', DEFAULT_NODE_IP)
    node_port = session.get('node_port', DEFAULT_NODE_PORT)
    
    status = get_node_status(node_ip, node_port)
    status["update"] = {"available": False} 
    
    return jsonify(status)

@app.route('/api/config', methods=['POST'])
def api_config():
    data = request.json or {}
    if 'ip' in data:
        session['node_ip'] = data['ip'].strip()
    if 'port' in data:
        session['node_port'] = data['port'].strip()
    return jsonify({"status": "ok"})

@app.route('/api/qrcode')
def api_qrcode():
    """Liefert das QR-Code Bild pi-qrcode.jpg aus dem Hauptverzeichnis aus"""
    from flask import send_file
    return send_file('pi-qrcode.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    # Liest den MONITOR_PORT dynamisch aus deiner .env
    port = int(os.environ.get('MONITOR_PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)

