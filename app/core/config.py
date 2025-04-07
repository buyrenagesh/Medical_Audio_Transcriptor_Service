import os

class Config:
    AZURE_SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
    AZURE_REGION = os.getenv("AZURE_REGION")
    AUDIO_FORMAT = "wav"  # or "mp3", depending on your needs
    MAX_AUDIO_LENGTH = 300  # maximum audio length in seconds
    INTERNAL_CODE_MAPPING = {
        "diagnosis": "DIA",
        "procedure": "PROC",
        "medication": "MED",
    }