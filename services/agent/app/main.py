import os
os.environ.setdefault("SERVICE_NAME", "agent-service")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routers.agent import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="Agent Service", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/agent")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "agent-service"}
