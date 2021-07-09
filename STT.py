from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey = 'RKA59KDihr0DOPDfRNN0Mzk_eNShVuknSw8bCIee3bLi'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/0ef14381-22d2-4d8e-977c-f9a785e6dce0'
# Setup Service
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)
# Perform conversion
with open('greeting.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()
print (res)
