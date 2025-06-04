# 🎤 SOVA TTS Demo Package

## Quick Start
1. Install dependencies: `pip3 install flask flask-cors pyyaml requests`
2. Run demo server: `python3 demo_app.py`
3. Open browser: http://localhost:8899/demo_interface.html
4. Run tests: `python3 test_demo.py`

## Files included:
- demo_app.py - Main demo server
- test_demo.py - Test script
- demo_interface.html - Web interface
- SOVA_TTS_Demo_Presentation.md - Full presentation
- SHARING_INSTRUCTIONS.md - Setup instructions
- *.wav - Demo audio files

## API Examples:
```bash
# Test synthesis
curl -X POST http://localhost:8899/synthesize/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Привет мир!", "voice": "Natasha"}'

# Check status  
curl http://localhost:8899/status
```

Enjoy the demo! 🎉
