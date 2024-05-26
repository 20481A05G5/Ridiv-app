from fastapi import APIRouter
from ..services.llm_service import get_gemini_response

router = APIRouter()

@router.post("/send-message/")
async def send_message(msg: str):
    response = get_gemini_response(msg)
    return {"response": response}