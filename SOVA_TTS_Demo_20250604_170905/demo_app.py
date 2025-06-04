from base64 import b64encode
import os
from flask import Flask, render_template, request, send_from_directory, url_for, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# Demo voices configuration
DEMO_VOICES = {
    "Natasha": {
        "description": "Female Russian voice",
        "sample_text": "Привет, мир! Это голос Наташи."
    },
    "Ruslan": {
        "description": "Male Russian voice", 
        "sample_text": "Добро пожаловать в SOVA TTS! Меня зовут Руслан."
    }
}

@app.route("/", methods=["GET"])
@cross_origin()
def index():
    return render_template("speechSynthesis.html", existing_models=DEMO_VOICES.keys())

@app.route("/synthesize/", methods=["POST"])
@cross_origin()
def synthesize():
    try:
        request_json = request.get_json()
        text = request_json.get("text", "")
        voice = request_json.get("voice", "Natasha")
        
        # For demo purposes, return one of the existing audio files
        audio_files = [f for f in os.listdir('.') if f.endswith('.wav')]
        
        if audio_files:
            # Use the first available audio file as demo output
            demo_file = audio_files[0]
            
            with open(demo_file, 'rb') as f:
                audio_bytes = f.read()
            
            result = {
                "response_code": 0,
                "response": [{
                    "text": text,
                    "voice": voice,
                    "response_audio": b64encode(audio_bytes).decode("utf-8"),
                    "response_audio_url": url_for("media_file", filename=demo_file),
                    "filename": demo_file,
                    "demo_mode": True,
                    "message": f"Demo mode: Using sample audio file '{demo_file}' for voice '{voice}'"
                }]
            }
        else:
            result = {
                "response_code": 1,
                "response": [{
                    "error": "No demo audio files available",
                    "demo_mode": True
                }]
            }
            
        return result
        
    except Exception as e:
        return {
            "response_code": 1,
            "response": [{
                "error": str(e),
                "demo_mode": True
            }]
        }

@app.route("/get_user_dict/", methods=["POST"])
@cross_origin()
def get_user_dict():
    return {
        "response_code": 0,
        "response": {
            "demo": "демо",
            "TTS": "тэ тэ эс",
            "SOVA": "сова"
        }
    }

@app.route("/update_user_dict/", methods=["POST"])
@cross_origin()
def update_user_dict():
    return {
        "response_code": 0,
        "response": "User dictionary updated (demo mode)"
    }

@app.route("/replace_user_dict/", methods=["POST"])
@cross_origin()
def replace_user_dict():
    return {
        "response_code": 0,
        "response": "User dictionary replaced (demo mode)"
    }

@app.route("/status", methods=["GET"])
@cross_origin()
def status():
    return {
        "status": "running",
        "mode": "demo",
        "voices": list(DEMO_VOICES.keys()),
        "description": "SOVA TTS Demo Mode - Using sample audio files"
    }

@app.route("/voices", methods=["GET"])
@cross_origin()
def voices():
    return {
        "voices": DEMO_VOICES
    }

@app.route("/media/<path:filename>", methods=["GET"])
@cross_origin()
def media_file(filename):
    return send_from_directory(".", filename, as_attachment=False)

if __name__ == "__main__":
    print("🎤 SOVA TTS Demo Server Starting...")
    print("📱 Demo Mode: Using sample audio files")
    print("🌐 Server will be available at: http://localhost:8899")
    print("🔧 Available voices:", list(DEMO_VOICES.keys()))
    
    # List available audio files
    audio_files = [f for f in os.listdir('.') if f.endswith('.wav')]
    if audio_files:
        print("🎵 Available demo audio files:", audio_files)
    else:
        print("⚠️  No audio files found for demo")
    
    app.run(host='0.0.0.0', port=8899, debug=True) 