import os;
import io;
from google.cloud import texttospeech
from google.cloud import speech


def text_to_speech(text):
    #Converts text to speech using the Text-to-Speech API.
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'rapid-potential-374916-59eb13218ba4.json'
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

# Test
# text_to_speech("Hello World")

def speech_to_text(mp3_file):
    #Converts speech to text using the Speech-to-Text API.
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'rapid-potential-374916-59eb13218ba4.json'
    client = speech.SpeechClient()

    with io.open(mp3_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=8000,
        language_code="en-US",
        use_enhanced=True,
        # A model must be specified to use enhanced model.
        model="phone_call",
    )

    response = client.recognize(config=config, audio=audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print("First alternative of result {}".format(i))
        print("Transcript: {}".format(alternative.transcript))
    
# Test
speech_to_text("test.mp3")