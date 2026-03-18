from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    if request.method == "POST":
        statement = request.form.get('statement', "")
        result = emotion_detector(statement)

        if result['dominant_emotion'] is None:
            response_text = "Invalid text! Please try again!"
        else:
            response_text = (
                f"For the given statement, the system response is "
                f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, 'joy': {result['joy']} and "
                f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
            )

        return render_template('index.html', result=response_text)
    else:
        return render_template('index.html', result="")

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
