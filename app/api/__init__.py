from fastapi import APIRouter

router = APIRouter()

from .endpoints import transcription

router.include_router(transcription.router, prefix="/process_audio", tags=["process_audio"])