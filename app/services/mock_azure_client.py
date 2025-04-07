class MockAzureSpeechToTextClient:
    def __init__(self):
        pass
    def transcribe_audio_stream(self, audio_stream):
        # Returning a mocked response as Azure account is not getting created.
        return {
            "status": "success",
            "transcription": "This is a mocked transcription of the audio file."
        }