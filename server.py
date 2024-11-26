"""this module is a server"""
from flask import Flask, request
from EmotionDetection import emotion_detector
app = Flask(__name__)
"""POST method"""
@app.route("/", methods = ['POST'])
def get_emotion():
    """get emotion by calling emotion_detector()"""
    text_to_analyze = request.get_data(as_text=True)
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Invalid text!Please try again"
    return result

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000)
