"""
Smart Editorial Assistant - Backend API

FastAPI application for AI-powered proofreading and editing support.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1 import proofread

app = FastAPI(
    title="Smart Editorial Assistant API",
    description="AI-Driven Writing & Proofing System Backend",
    version="0.1.0",
)

# CORS設定（Chrome拡張機能からのアクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開発時は全許可、本番では適切に制限
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API v1 ルーターを登録
app.include_router(
    proofread.router,
    prefix="/api/v1",
    tags=["proofread"],
)


@app.get("/")
async def root():
    """ヘルスチェック用エンドポイント"""
    return {"status": "ok", "message": "Smart Editorial Assistant API is running"}


@app.get("/health")
async def health_check():
    """ヘルスチェック"""
    return {"status": "healthy"}
