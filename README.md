# Medical Transcription Backend

This project is a backend service for converting doctor voice dictations into structured medical data using Azure's Speech-to-Text API. It exposes a RESTful API that allows audio uploads or streams, transcribes the audio, identifies key medical entities, matches phrases with internal codes, and returns structured results in JSON format.

## Features

- Audio transcription using Azure's Speech-to-Text API
- Extraction of key medical entities from transcriptions
- Mapping of transcribed phrases to internal medical codes
- RESTful API for audio uploads and streaming

## Project Structure

```
medical-transcription-backend
├── app
│   ├── api
│   │   ├── endpoints
│   ├── core
│   ├── models
│   ├── services
│   ├── utils
│   └── main.py
├── tests
├── requirements.txt
├── .env
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd medical-transcription-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables in the `.env` file:
   ```
   AZURE_SPEECH_KEY=<your_azure_speech_key>
   AZURE_REGION=<your_azure_region>
   ```

## Usage

To run the application, execute the following command:
```
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Documentation

### Transcription Endpoint

- **POST /transcribe**
  - Description: Upload audio for transcription.
  - Request Body: Audio file (WAV, MP3, etc.)
  - Response: JSON object containing transcribed text and structured medical data.

### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/transcribe" -F "file=@path_to_audio_file"
```

### Example Response

```json
{
  "transcription": "Patient shows signs of improvement.",
  "medical_data": {
    "diagnosis": "Improvement",
    "procedure_code": "12345"
  }
}
```

## Testing

To run the tests, use the following command:
```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.