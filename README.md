
# Interactive Chatbot with Hand Gesture Recognition 🤖👋  

**Part of a broader initiative to enhance app interactivity through AI-driven image recognition.**  

This module adds **real-time hand gesture detection** to chatbots, enabling:  
- 👍/👎 Reactions via thumb position  
- Voice feedback integration  
- Seamless integration with interactive apps  

---

##  Key Features  
- **Gesture-to-Action Mapping**: Converts hand positions (thumb up/down) to user feedback.  
- **Voice Responses**: Uses TTS (Text-to-Speech) for dynamic interaction.  
- **Low-Latency Detection**: Powered by **MediaPipe** and **OpenCV** for real-time performance.  

---

## 🛠️ Technologies  
- `MediaPipe Hands` for gesture tracking  
- `OpenCV` for camera stream processing  
- `pyttsx3` for voice feedback  

---

## 🚀 Installation  
```bash  
pip install opencv-python mediapipe pyttsx3  
```  

---

## 🖐️ Usage  
Run the detector:  
```bash  
python gesture_detector.py  
```  
- Show your hand to the camera.  
- Thumb **UP** → "Liked" + voice confirmation ✅  
- Thumb **DOWN** → "Disliked" + feedback ❌  

---

## 🌟 Why This Matters  
This module demonstrates how **image recognition** can bridge chatbots and real-world interactions, enabling:  
- Accessible UI/UX for diverse users  
- Enhanced engagement in apps/games  
- Foundation for AR/VR gesture controls 
