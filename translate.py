from google.cloud import translate
from config import *
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= KEY_PATH

def translate_text(text="YOUR_TEXT_TO_TRANSLATE", src_lang= "en-US", targ_lang= "ja"):
    """Translating Text."""
    project_id= PROJECT_ID
    
    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": src_lang,
            "target_language_code": targ_lang,
        }
    )

    # Display the translation for each input text provided
    # for translation in response.translations:
        # print("Translated text: {}".format(translation.translated_text))
    return response.translations[0].translated_text

def detect_language(text):
    """Detecting the language of a text string."""
    project_id=PROJECT_ID

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.detect_language(
        content="Hello World",
        parent=parent,
        mime_type="text/plain",  # mime types: text/plain, text/html
    )

    # Display list of detected languages sorted by detection confidence.
    # The most probable language is first.
    # for language in response.languages:
    #     # The language detected
    #     print("Language code: {}".format(language.language_code))
    #     # Confidence of detection result for this language
    #     print("Confidence: {}".format(language.confidence))
    
    return response.languages[0].language_code


def get_translated_text(text, targ_lang):
    return translate_text(text, detect_language(text), targ_lang)





