#!/usr/bin/env python3
"""
SOVA TTS Demo Test Script
This script demonstrates the functionality of the SOVA TTS system
"""

import requests
import json
import time
import os

def test_sova_tts_demo():
    base_url = "http://localhost:8899"
    
    print("🎤 SOVA TTS Demo Test")
    print("=" * 50)
    
    # Test 1: Check server status
    print("\n1️⃣ Testing server status...")
    try:
        response = requests.get(f"{base_url}/status")
        if response.status_code == 200:
            status = response.json()
            print(f"✅ Server is running: {status}")
        else:
            print(f"❌ Server returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to server: {e}")
        return False
    
    # Test 2: Get available voices
    print("\n2️⃣ Getting available voices...")
    try:
        response = requests.get(f"{base_url}/voices")
        if response.status_code == 200:
            voices = response.json()
            print(f"✅ Available voices: {voices}")
        else:
            print(f"❌ Failed to get voices: {response.status_code}")
    except Exception as e:
        print(f"❌ Error getting voices: {e}")
    
    # Test 3: Test text synthesis
    print("\n3️⃣ Testing text synthesis...")
    test_texts = [
        "Привет, мир! Это тест системы SOVA TTS.",
        "Добро пожаловать в демонстрацию голосового синтеза.",
        "Hello, this is a test of the SOVA TTS system."
    ]
    
    voices = ["Natasha", "Ruslan"]
    
    for i, text in enumerate(test_texts, 1):
        voice = voices[i % len(voices)]
        print(f"\n   Test {i}: Text='{text}', Voice='{voice}'")
        
        try:
            payload = {
                "text": text,
                "voice": voice,
                "rate": 1.0,
                "pitch": 1.0,
                "volume": 0.0
            }
            
            response = requests.post(
                f"{base_url}/synthesize/",
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload)
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"   ✅ Synthesis successful: {result.get('response_code', 'unknown')}")
                if result.get("response"):
                    resp = result["response"][0]
                    if resp.get("demo_mode"):
                        print(f"   📝 Demo message: {resp.get('message', 'N/A')}")
                    if resp.get("filename"):
                        print(f"   🎵 Audio file: {resp.get('filename')}")
            else:
                print(f"   ❌ Synthesis failed: {response.status_code}")
                print(f"   Response: {response.text}")
                
        except Exception as e:
            print(f"   ❌ Error during synthesis: {e}")
    
    # Test 4: Test user dictionary
    print("\n4️⃣ Testing user dictionary...")
    try:
        # Get current dictionary
        response = requests.post(f"{base_url}/get_user_dict/", 
                               headers={"Content-Type": "application/json"},
                               data=json.dumps({"voice": "Natasha"}))
        
        if response.status_code == 200:
            dict_data = response.json()
            print(f"✅ Current user dictionary: {dict_data}")
        
        # Update dictionary
        new_dict = {"test": "тест", "demo": "демо", "AI": "ай ай"}
        response = requests.post(f"{base_url}/update_user_dict/",
                               headers={"Content-Type": "application/json"},
                               data=json.dumps({"voice": "Natasha", "user_dict": new_dict}))
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Dictionary update: {result}")
            
    except Exception as e:
        print(f"❌ Error testing user dictionary: {e}")
    
    print("\n🎯 Demo test completed!")
    print("\n💡 You can now:")
    print(f"   • Open http://localhost:8899 in your browser")
    print(f"   • Use curl/Postman to test the API endpoints")
    print(f"   • Modify the demo_app.py for custom functionality")
    
    return True

if __name__ == "__main__":
    # Wait a moment for server to start
    print("Waiting for server to start...")
    time.sleep(3)
    test_sova_tts_demo() 