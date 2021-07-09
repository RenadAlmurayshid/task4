
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('tpct-otFtstj59IfmmeZZsfgs5BGUMH4zLWo-IzZT1im')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/8ee596bb-765a-429f-83e5-13d69fa8e916')

with open('sayinghello.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Hello ',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'
        ).get_result().content)

