from flask import Flask, jsonify, request
import assemblyai as aai

app = Flask(__name__)


def speechToText(audioUrl):
    aai.settings.api_key = "20ac7bc85f554848a2218af7127a33e2"
    transcriber = aai.Transcriber()

    config = aai.TranscriptionConfig(speaker_labels=True)
    transcript = transcriber.transcribe(audioUrl, config)

    return transcript.text


@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello'})


@app.route('/api/speechToText', methods=['POST'])
def speechToTexApi():
    audio_url = request.json.get('audioUrl')
    if not audio_url:
        return jsonify({'error': 'Thiếu đường dẫn âm thanh'}), 400

    text = speechToText(audio_url)
    return jsonify({'text': text}), 200


if __name__ == '__main__':
    app.run(debug=True)
