import requests
import json
def emotion_detector(text_to_analyze):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=input)
    if response.status_code == 200:
        try: 
            data = response.text
            emotionPredictions = json.loads(data)["emotionPredictions"]
            if len(emotionPredictions) > 0:
                emotion = emotionPredictions[0]["emotion"]
                anger_score = emotion["anger"]
                disgust_score = emotion["disgust"]
                fear_score = emotion["fear"]
                joy_score = emotion["joy"]
                sadness_score = emotion["sadness"]
                scores = list(emotion.values())
                max_score = max(scores)
                emotion_found = None
                for key, score in emotion.items():
                    if score == max_score:
                        emotion_found = key
                        break
                return {
                        'anger': anger_score,
                        'disgust': disgust_score,
                        'fear': fear_score,
                        'joy': joy_score,
                        'sadness': sadness_score,
                        'dominant_emotion': emotion_found
                        }
        except ValueError:
            print("Error of json")
    elif response.status_code == 400:
          return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                } 
    else:
        return "Error: No detect emotion"