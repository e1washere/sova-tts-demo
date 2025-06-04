#!/usr/bin/env python3
"""
Script to package SOVA TTS demo files for sharing
"""

import os
import shutil
import zipfile
from datetime import datetime

def create_demo_package():
    """Create a demo package with all necessary files"""
    
    # Files to include in the demo package
    demo_files = [
        'demo_app.py',
        'test_demo.py', 
        'demo_interface.html',
        'SOVA_TTS_Demo_Presentation.md',
        'SHARING_INSTRUCTIONS.md',
        'tts_output.wav',
        'output.wav'
    ]
    
    # Create package directory
    package_name = f"SOVA_TTS_Demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    package_dir = f"./{package_name}"
    
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    
    os.makedirs(package_dir)
    
    print(f"📦 Creating demo package: {package_name}")
    
    # Copy files
    for file in demo_files:
        if os.path.exists(file):
            shutil.copy2(file, package_dir)
            print(f"✅ Added: {file}")
        else:
            print(f"⚠️  Missing: {file}")
    
    # Create README for the package
    readme_content = """# 🎤 SOVA TTS Demo Package

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
curl -X POST http://localhost:8899/synthesize/ \\
  -H "Content-Type: application/json" \\
  -d '{"text": "Привет мир!", "voice": "Natasha"}'

# Check status  
curl http://localhost:8899/status
```

Enjoy the demo! 🎉
"""
    
    with open(f"{package_dir}/README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ Added: README.md")
    
    # Create zip archive
    zip_filename = f"{package_name}.zip"
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, package_dir)
                zipf.write(file_path, arcname)
    
    print(f"📦 Created archive: {zip_filename}")
    
    # Generate sharing summary
    summary = f"""
🎉 SOVA TTS Demo Package Created!

📁 Package Directory: {package_dir}/
📦 Archive File: {zip_filename}

📧 How to share:
1. Send the zip file: {zip_filename}
2. Or share the entire folder: {package_dir}/

🚀 Recipient instructions:
1. Extract files
2. pip3 install flask flask-cors pyyaml requests
3. python3 demo_app.py
4. Open http://localhost:8899/demo_interface.html

✅ Demo includes:
- Working TTS API server
- Web interface demonstration
- Test scripts
- Full documentation in Russian
- API examples and curl commands

Total package size: {get_directory_size(package_dir):.1f} MB
"""
    
    print(summary)
    
    # Save summary to file
    with open(f"{package_name}_SUMMARY.txt", 'w', encoding='utf-8') as f:
        f.write(summary)
    
    return package_dir, zip_filename

def get_directory_size(directory):
    """Calculate directory size in MB"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size / (1024 * 1024)

if __name__ == "__main__":
    create_demo_package() 