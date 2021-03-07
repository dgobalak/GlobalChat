from google.cloud import translate
from config import *
import os
import googletrans


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH


def translate_text(text="YOUR_TEXT_TO_TRANSLATE", src_lang="en-US", targ_lang="ja"):
    """Translating Text."""
    project_id = PROJECT_ID

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

    return response.translations[0].translated_text


def detect_language(text):
    """Detecting the language of a text string."""
    project_id = PROJECT_ID

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.detect_language(
        content=text,
        parent=parent,
        mime_type="text/plain",  # mime types: text/plain, text/html
    )

    return response.languages[0].language_code


def get_translated_text(text, targ_lang):
    src_lang = detect_language(text)
    if src_lang != targ_lang:
        return translate_text(text, detect_language(text), targ_lang)
    return text

def get_supported_languages():
    """Getting a list of supported language codes."""

    all_languages = {v: k for k, v in googletrans.LANGUAGES.items()}

    return all_languages

def get_language_code(language_name):
    return get_supported_languages()[language_name.lower()]

def get_language_name(code):
    all_languages = {k: v for k, v in googletrans.LANGUAGES.items()}
    return all_languages[code]


