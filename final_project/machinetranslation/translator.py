import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText) :
    if englishText.strip()=="":
        return englishText
    frenchTexts=language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText=frenchTexts["translations"][0]['translation']
    return frenchText

def frenchToEnglish(frenchText) :
    if frenchText.strip()=="":
        return frenchText
    englishTexts=language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText=englishTexts["translations"][0]['translation']
    return englishText