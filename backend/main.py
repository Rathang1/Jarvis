from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from backend.api.routes import router

# Load .env file so ANTHROPIC_API_KEY is available
load_dotenv()

app = FastAPI(title="Jarvis API")

# CORS lets your frontend (running on a different port) talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this later in production
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)