from fastapi.responses import JSONResponse

def create_error_response(error_code: str, error_message: str, resource: str, resolution: str):
    return JSONResponse(
        content={
            "error_code": error_code,
            "error_message": error_message,
            "resource": resource,
            "resolution": resolution,
        },
        status_code=400 
    )