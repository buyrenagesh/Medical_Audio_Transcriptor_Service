from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig
import os

class AzureSpeechToTextClient:
    def __init__(self):
        self.speech_key = os.getenv("AZURE_SPEECH_KEY")
        self.service_region = os.getenv("AZURE_SERVICE_REGION")
        self.speech_config = SpeechConfig(subscription=self.speech_key, region=self.service_region)

    def transcribe_audio_stream(self, audio_stream):
        audio_config = AudioConfig(stream=audio_stream)
        recognizer = SpeechRecognizer(speech_config=self.speech_config, audio_config=audio_config)

        result = recognizer.recognize_once()
        return self._handle_result(result)

    def transcribe_audio_file(self, audio_file_path):
        audio_config = AudioConfig(filename=audio_file_path)
        recognizer = SpeechRecognizer(speech_config=self.speech_config, audio_config=audio_config)

        result = recognizer.recognize_once()
        return self._handle_result(result)

    def _handle_result(self, result):
        if result.reason == result.Reason.RecognizedSpeech:
            return {
                "status": "success",
                "transcription": result.text
            }
        elif result.reason == result.Reason.NoMatch:
            return {
                "status": "error",
                "error": "No speech could be recognized."
            }
        elif result.reason == result.Reason.Canceled:
            cancellation_details = result.cancellation_details
            return {
                "status": "error",
                "error": f"Speech recognition canceled: {cancellation_details.reason}",
                "details": cancellation_details.error_details if cancellation_details.error_details else None
            }