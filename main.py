# main.py: Init server and run it with Uvicorn. This file is the entry point for the application.
import logging
import os
from typing import Optional

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

# Init logging for files main.py
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("main.log"),
        logging.StreamHandler(),
    ],
)

load_dotenv()


class Server:
    def __init__(self) -> None:
        self.app = FastAPI(
            title="Clip engine API",
            description="This API is responsible for providing endpoints to interact with the clip engine.",
            version="0.0.1",
            middleware=[
                Middleware(
                    CORSMiddleware,
                    allow_origins=["*"],
                    allow_methods=["*"],
                    allow_headers=["*"],
                )
            ],
        )

        self.setup_routes()

    def setup_routes(self):
        # Health check route
        from src.api.routes.index import router as index_router

        self.app.include_router(index_router)

        from src.api.routes.download_youtube import router as download_router

        self.app.include_router(download_router)

    def run(self, host: str = "0.0.0.0", port: int = 8000):
        INITIALIZE_MODE = os.getenv("INITIALIZE_MODE", "production")

        # Pega valores do ENV ou usa os defaults passados no argumento
        run_host = os.getenv("HOST", host)
        run_port = int(os.getenv("PORT", port))

        if INITIALIZE_MODE == "DEVOPMENT_MODE":
            logging.info("API is running in development mode")
            uvicorn.run("main:app", host=run_host, port=run_port, reload=True)
        else:
            logging.info("API is running in production mode")
            uvicorn.run("main:app", host=run_host, port=run_port)


# Init serve and run
server_instance = Server()
app = server_instance.app  # Isso expõe o objeto para o Uvicorn encontrar "main:app"

if __name__ == "__main__":
    logging.info("Starting the Clip engine API server...")
    server_instance.run()
