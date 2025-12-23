"""
Gemini API Service Stub

This module will handle communication with Google Gemini API
for AI-powered proofreading functionality.
"""
from typing import Any


async def proofread_with_gemini(content: str) -> list[dict[str, Any]]:
    """
    校閲処理をGemini APIで実行する（スタブ関数）
    
    将来的にはここでGemini APIを呼び出し、
    誤字脱字、法務チェック、ハルシネーション検出などを行う。
    
    Args:
        content: 校閲対象のテキスト
        
    Returns:
        校閲結果のリスト（各項目は ProofreadItem に変換可能な辞書）
    
    TODO:
        - Gemini API クライアントの初期化
        - 校閲用プロンプトの設計
        - レスポンスのパース処理
    """
    # スタブ実装: 空のリストを返す
    # 実際の実装時はここでGemini APIを呼び出す
    raise NotImplementedError("Gemini API integration is not yet implemented")


async def generate_proofreading_prompt(content: str) -> str:
    """
    校閲用のプロンプトを生成する（スタブ関数）
    
    Args:
        content: 校閲対象のテキスト
        
    Returns:
        Gemini APIに送信するプロンプト文字列
        
    TODO:
        - カテゴリ（TYPO, LEGAL, HALLUCINATION, STYLE）ごとの指示
        - JSON形式での出力指示
    """
    raise NotImplementedError("Prompt generation is not yet implemented")
