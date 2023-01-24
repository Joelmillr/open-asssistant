from flask import Flask

app = Flask(__name__)

@app.route("/arduino")
def arduino_test_route():
    print("route was triggered")
    return "Hello World!"

# @app.route("/speech-to-text")
# def voice_request(mp3_file):
#     #Converts speech to text using the Speech-to-Text API.
#     text = speech_to_text(mp3_file)

#     # Send chat gpt api call
#     # TODO
#     response = chat_gpt_api_call(text)

#     # convert text to speech
#     mp3_file = text_to_speech(response)

#     return mp3_file