from fastapi import FastAPI
from app.routers import chat  # Absolute import

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only; specify your frontend's URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)  # Ensure you're using the correct attribute
