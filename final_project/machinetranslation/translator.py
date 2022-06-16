import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

#import json
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)
def englishtofrench(englishtext):
    #write the code here
    if englishtext is None:
        return None
    out = language_translator.translate(text=englishtext,model_id='en-fr').get_result()
    return out['translations'][0]['translation']

def frenchtoenglish(frenchtext):
    #write the code here
    if frenchtext is None:
        return None
    out = language_translator.translate(text=frenchtext,model_id='fr-en').get_result()
    return out['translations'][0]['translation']