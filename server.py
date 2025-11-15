from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract from the response
    response_display = ("For the given statement, the system response is "
     + "'anger': " + str(response['anger'])
     + " ', disgust': " + str(response['disgust'])
     + " ', fear': " + str(response['fear'])
     + " ', joy': " + str(response['joy'])
     + " and 'sadness': " + str(response['sadness'])
     + ". The dominant emotion is " + str(response['dominant_emotion']) + "."
    )
    # Return a formatted string
    # Check if the label is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Try again."
    else:
        return response_display

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)