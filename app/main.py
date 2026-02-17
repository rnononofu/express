from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes import router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# 静的ファイル配信
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルート登録
app.include_router(router)
