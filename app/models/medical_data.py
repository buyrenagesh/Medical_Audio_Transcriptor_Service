from pydantic import BaseModel
from typing import List, Optional

class MedicalEntity(BaseModel):
    name: str
    code: str
    description: Optional[str] = None

class MedicalData(BaseModel):
    transcription: str
    entities: List[MedicalEntity]

class MedicalProcedure(BaseModel):
    procedure_name: str
    procedure_code: str
    entities: List[MedicalEntity]

class Diagnosis(BaseModel):
    diagnosis_name: str
    diagnosis_code: str
    entities: List[MedicalEntity]

class TranscriptionResult(BaseModel):
    transcribed_text: str
    procedures: List[MedicalProcedure]
    diagnoses: List[Diagnosis]