"""
Proofread API Endpoint

POST /api/v1/proofread - Mock endpoint that returns sample proofreading results.
"""
import uuid
from fastapi import APIRouter

from models.schemas import (
    ProofreadRequest,
    ProofreadResponse,
    ProofreadItem,
    LocationIndex,
    CategoryType,
    StatusType,
)

router = APIRouter()


def generate_mock_proofread_items(content: str) -> list[ProofreadItem]:
    """
    モック用の校閲結果を生成する
    
    Args:
        content: 校閲対象のテキスト
        
    Returns:
        サンプルの校閲結果リスト
    """
    # ダミーデータを返す
    mock_items = [
        ProofreadItem(
            id=str(uuid.uuid4()),
            original_text="サンプル文章",
            suggested_text="サンプルの文章",
            category=CategoryType.TYPO,
            reason="「の」が抜けている可能性があります。",
            location_index=LocationIndex(start_index=0, end_index=6),
            status=StatusType.PENDING,
        ),
        ProofreadItem(
            id=str(uuid.uuid4()),
            original_text="必ず成功します",
            suggested_text="成功する可能性が高いです",
            category=CategoryType.LEGAL,
            reason="断定的な表現は景品表示法に抵触する恐れがあります。",
            location_index=LocationIndex(start_index=10, end_index=17),
            status=StatusType.PENDING,
        ),
        ProofreadItem(
            id=str(uuid.uuid4()),
            original_text="AIが全てを解決します",
            suggested_text="AIが課題解決を支援します",
            category=CategoryType.HALLUCINATION,
            reason="過度な表現は事実に基づかない可能性があります。",
            location_index=LocationIndex(start_index=20, end_index=32),
            status=StatusType.PENDING,
        ),
    ]
    return mock_items


@router.post("/proofread", response_model=ProofreadResponse)
async def proofread_document(request: ProofreadRequest) -> ProofreadResponse:
    """
    ドキュメントの校閲を実行する（モックAPI）
    
    現在はダミーデータを返すモック実装。
    将来的には services/gemini_service.py を呼び出して
    実際のAI校閲を行う。
    
    Args:
        request: 校閲リクエスト（document_id, content）
        
    Returns:
        校閲結果（Shared Data Schema に準拠）
    """
    # モックデータを生成
    items = generate_mock_proofread_items(request.content)
    
    return ProofreadResponse(
        document_id=request.document_id,
        items=items,
    )
