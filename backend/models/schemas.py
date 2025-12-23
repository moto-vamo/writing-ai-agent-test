"""
Pydantic models for the proofread API.
Based on the Shared Data Schema defined in README.md.
"""
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
import uuid


class CategoryType(str, Enum):
    """校閲指摘のカテゴリ"""
    TYPO = "TYPO"
    LEGAL = "LEGAL"
    HALLUCINATION = "HALLUCINATION"
    STYLE = "STYLE"


class StatusType(str, Enum):
    """指摘のステータス"""
    PENDING = "PENDING"
    FIXED = "FIXED"
    IGNORED = "IGNORED"


class LocationIndex(BaseModel):
    """テキスト内の位置情報"""
    start_index: int = Field(..., description="開始インデックス")
    end_index: int = Field(..., description="終了インデックス")


class ProofreadItem(BaseModel):
    """校閲結果の個別項目"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="一意識別子")
    original_text: str = Field(..., description="指摘対象の原文テキスト")
    suggested_text: str = Field(..., description="修正案のテキスト")
    category: CategoryType = Field(..., description="指摘カテゴリ")
    reason: str = Field(..., description="AIによる指摘理由")
    location_index: LocationIndex = Field(..., description="テキスト内の位置")
    status: StatusType = Field(default=StatusType.PENDING, description="指摘のステータス")


class ProofreadResponse(BaseModel):
    """校閲APIのレスポンス"""
    document_id: str = Field(..., description="ドキュメントID")
    items: list[ProofreadItem] = Field(default_factory=list, description="校閲結果リスト")


class ProofreadRequest(BaseModel):
    """校閲APIのリクエスト"""
    document_id: str = Field(..., description="ドキュメントID")
    content: str = Field(..., description="校閲対象のテキスト")
