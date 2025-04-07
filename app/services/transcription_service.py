from fastapi import UploadFile
from app.core.azure_client import AzureSpeechToTextClient
from app.utils.entity_extraction import extract_medical_entities
from app.models.medical_data import MedicalData
from app.utils.error_utils import create_error_response
import json
from app.services.mock_azure_client import MockAzureSpeechToTextClient

class TranscriptionService:
    def __init__(self, use_mock: bool = False):
        if use_mock:
            self.azure_client = MockAzureSpeechToTextClient()
        else:
            self.azure_client = AzureSpeechToTextClient()

    def transcribe_audio(self, audio_file: UploadFile):
        transcription_result = self.azure_client.transcribe_audio_stream(audio_file.file)
        if transcription_result.get("status") == "error":
            return create_error_response(
                error_code="transcription_service_error_063",
                error_message=transcription_result.get("error", "Unknown error occurred."),
                resource="Medical_Audio_Transcriptor_Service/app/services/transcription_service",
                resolution="Check audio file and try again"
            )
        transcription = transcription_result.get("transcription", "")
        return self.process_transcription(transcription)

    def process_transcription(self, transcription: str):
        medical_entities = extract_medical_entities(transcription) 
        structured_data = MedicalData(transcription=transcription, entities=medical_entities)
        return json.loads(structured_data.json())