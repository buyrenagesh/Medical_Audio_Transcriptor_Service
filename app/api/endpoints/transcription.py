from fastapi import APIRouter, UploadFile, File, Header
from typing import Optional
from app.services.transcription_service import TranscriptionService
from app.models.medical_data import MedicalData
from app.utils.error_utils import create_error_response 

router = APIRouter()
transcription_service = TranscriptionService(use_mock=True) # Set to True for mock service

# Allowed MIME types
ALLOWED_MIME_TYPES = ["audio/mpeg", "audio/wav"]  # .mp3, .wav

@router.post("/process_audio", response_model=MedicalData)
async def process_audio_file(
    file: UploadFile = File(...),
    processing_mode: Optional[str] = Header(None)  
):
    if file.content_type not in ALLOWED_MIME_TYPES:
        return create_error_response(
            error_code="transcription_service_001",
            error_message="Invalid Format",
            resource="Medical_Audio_Transcriptor_Service/app/api/endpoints",
            resolution="Add Correct response"
        )

    if processing_mode == "trigger":
        transcription = ""
        entities = []
        chunk_size = 1024  
        while chunk := await file.read(chunk_size):
            partial_transcription, partial_entities = transcription_service.transcribe_audio(chunk)
            transcription += partial_transcription
            entities.extend(partial_entities)
    else:
        audio_data = await file.read()
        transcription, entities = transcription_service.transcribe_audio(audio_data)
    
    return MedicalData(transcription=transcription, entities=entities)