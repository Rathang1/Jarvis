from fastapi import APIRouter
from pydantic import BaseModel
from backend.agent.jarvis import create_jarvis

router = APIRouter()

# One shared agent for now (we'll make this per-session later)
jarvis = create_jarvis()

# This defines the shape of the request body
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    POST /chat
    Send a message to Jarvis, get a response back.
    The agent automatically remembers previous messages.
    """
    response = jarvis(request.message)
    return ChatResponse(reply=str(response))

@router.get("/health")
async def health():
    """
    GET /health
    Simple check to confirm the API is running.
    """
    return {"status": "Jarvis is online"}