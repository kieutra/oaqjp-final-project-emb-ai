from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector
app = Flask(__name__)

@app.route("/", methods = ['POST'])
def emotionDetection():
    text_to_analyze = request.get_data(as_text=True)       
    result = emotion_detector(text_to_analyze);
    if result["dominant_emotion"] == None:
        return "Invalid text!Please try again"
    return result

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000)