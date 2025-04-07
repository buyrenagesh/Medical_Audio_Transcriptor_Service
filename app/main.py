from fastapi import FastAPI
from app.api.endpoints.transcription import router as transcription_router

appFastApi = FastAPI()

appFastApi.include_router(transcription_router, prefix="/api", tags=["transcription"])

@appFastApi.get("/")
def read_root():
    return {"message": "Started Medical Audio Transcriptor API"}