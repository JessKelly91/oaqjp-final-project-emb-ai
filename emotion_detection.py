import requests;

def emotion_detector(text_to_analyze):
    """
    Analyze text to detect emotions using IBM Watson's emotion analysis service.
    
    This function sends a request to Watson's emotion prediction API to analyze the
    emotional content of the provided text. It returns scores for five basic emotions
    and identifies the dominant emotion.
    
    Args:
        text_to_analyze (str): The text string to be analyzed for emotional content.
        
    Returns:
        dict: A dictionary containing emotion scores and dominant emotion with the following keys:
            - 'anger' (float): Score for anger emotion (0.0 to 1.0)
            - 'disgust' (float): Score for disgust emotion (0.0 to 1.0)
            - 'fear' (float): Score for fear emotion (0.0 to 1.0)
            - 'joy' (float): Score for joy emotion (0.0 to 1.0)
            - 'sadness' (float): Score for sadness emotion (0.0 to 1.0)
            - 'dominant_emotion' (str): The emotion with the highest score
            
        If the request fails (status code 400), all values will be set to 'None'.
        
    Example:
        >>> result = emotion_detector("I am very happy today!")
        >>> print(result['dominant_emotion'])
        'joy'
        >>> print(result['joy'])
        0.8945
        
    Note:
        Requires internet connection to access Watson's emotion analysis API.
        Invalid or empty text input will result in a 400 status code response.
    """
    base_url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }

    raw_document = {
        "raw_document":{
            "text": text_to_analyze
        }
    }

    res = requests.post(base_url, headers=headers, json=raw_document)

    if res.status_code == 200:
        res_json = res.json()
        emotions = res_json['emotionPredictions'][0]['emotion']
        
        emotions_response = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': max(emotions, key=emotions.get)
        }

        return emotions_response
        
    elif res.status_code == 400:
        emotions_response = {
            'anger': 'None',
            'disgust': 'None',
            'fear': 'None',
            'joy': 'None',
            'sadness': 'None',
            'dominant_emotion': 'None'
        }
        
        return emotions_response