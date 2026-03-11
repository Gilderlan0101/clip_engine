import logging
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, status

# Logging configuration for index.py
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("index.log"),
        logging.StreamHandler(),
    ],
)

router = APIRouter(prefix="/api", tags=["Health Check"])


# Return the current server time in ISO 8601 format Brazil
@router.get("/health", status_code=status.HTTP_200_OK)
def healthRouter():
    try:
        current_time = datetime.now(timezone.utc).isoformat()
        logging.info(f"Health check requested at {current_time}")
        return {
            "status": "ok",
            "server_time": current_time,
            "message": "API is healthy and running",
            "server": "Clip Server",
        }
    except Exception as e:
        logging.error(f"Error during health check: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
