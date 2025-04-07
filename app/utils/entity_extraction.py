from typing import List, Dict
import re

INTERNAL_CODES = {
    "cold": "Gen01",
    "fever": "Gen02",
    "headache": "Gen03",
    "diabetes": "Endo01",
    "hypertension": "Cardio01",
    "epilepsy": "Neuro01",
    "stroke": "Neuro02",
    "asthma": "Resp01",
    "pneumonia": "Resp02",
    "kidney stone": "Uro01"
}

def extract_medical_entities(transcription: str) -> List[Dict[str, str]]:
    entities = []

    transcription_lower = transcription.lower()
    
    for term, code in INTERNAL_CODES.items():
        if re.search(r'\b' + re.escape(term) + r'\b', transcription_lower):
            entities.append({
                "term": term,
                "code": code
            })
    
    return entities

def match_entities_with_codes(entities: List[Dict[str, str]]) -> Dict[str, str]:
    matched_entities = {}
    
    for entity in entities:
        matched_entities[entity["term"]] = entity["code"]
    
    return matched_entities