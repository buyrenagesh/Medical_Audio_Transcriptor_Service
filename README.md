Medical Audio Transcription Backend

This project is a backend service for converting doctor voice dictations into structured medical data using Azure's Speech-to-Text API. It exposes a RESTful API that allows audio uploads or streams, transcribes the audio, identifies key medical entities, matches phrases with internal codes, and returns structured results in JSON format.

Features

Audio transcription using Azure's Speech-to-Text API
Extraction of key medical entities from transcriptions
Mapping of transcribed phrases to internal medical codes
RESTful API for audio uploads and streaming

Installation

1. Clone the repository
2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate

3. Install the required packages:
   pip install -r requirements.txt

4. Set up environment variables in the .env file:
   AZURE_SPEECH_KEY=<your_azure_speech_key>
   AZURE_REGION=<your_azure_region>
   Currently we are using mock Azure API.
   For actual deployment change Transcription_service.py line from service = TranscriptionService(use_mock=True) to service = TranscriptionService()


To run the application, execute the following command:
uvicorn app.main:app --reload


The API will be available at http://127.0.0.1:8000




Transcription Endpoint

POST /process_audio
  Description: Upload audio for transcription.
  Request Body: Audio file (WAV/ MP3)
  Response: JSON object containing transcribed text and structured
  medical data.



curl -X POST "http://127.0.0.1:8000/process_audio" -F "file=@path_to_audio_file"


