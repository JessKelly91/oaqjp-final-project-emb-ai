"""
Emotion Detection Web Server

This Flask web application provides a user interface and REST API for emotion detection
using IBM Watson's Natural Language Processing service. Users can submit text through
a web interface and receive emotional analysis results.
"""

from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector  # pylint: disable=import-error

app = Flask("Emotion Detection")

@app.route('/')
def render_index_page():
    """
    Render the main index page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    API endpoint for emotion detection analysis.
    
    This route accepts text input via GET request query parameter and returns
    emotion analysis results in JSON format. If the input text is invalid,
    it returns an error message with HTTP 400 status.
    
    Query Parameters:
        textToAnalyze (str): The text to be analyzed for emotional content.
        
    Returns:
        flask.Response: JSON response containing emotion scores and dominant emotion,
                       or error message with 400 status for invalid input.
                       
    Example:
        GET /emotionDetector?textToAnalyze=I%20am%20happy
        
        Response (200):
        {
            "anger": 0.1,
            "disgust": 0.05,
            "fear": 0.08,
            "joy": 0.85,
            "sadness": 0.02,
            "dominant_emotion": "joy"
        }
        
        Response (400):
        "Invalid text! Please try again!"
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == 'None':
        return "Invalid text! Please try again!", 400

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
