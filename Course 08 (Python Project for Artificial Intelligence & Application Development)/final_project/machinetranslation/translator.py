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
    version='2022-08-03',
    authenticator=authenticator
)

language_translator.set_service_url(url)

languages = language_translator.list_languages().get_result()

def english_to_french(english_text):
    englishtranslation=language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    return englishtranslation.get("translations")[0].get("translation")

def french_to_english(french_text):
    frenchtranslation=language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    return frenchtranslation.get("translations")[0].get("translation")
