# Smart Editorial Assistant (AI-Driven Writing & Proofing System)

## 1. Project Overview
このプロジェクトは、編集・ライティング業務の効率化と自動化を目指すシステム開発です。
Google Docsを中心としたワークフローにおいて、AIを活用した「校閲支援（Proofing）」と「ライティング自動化（Writing Automation）」の2つの機能を提供します。

### Key Objectives
1.  **校閲工数の削減:** Chrome拡張機能（Side Panel）を用い、原文とAI指摘を並列表示。視線移動をなくし、ワンクリックで修正可能にする。
2.  **ライティングの自動化:** 将来的にはAIエージェントが記事構成・執筆を行い、校閲機能とシームレスに連携する。
3.  **AI駆動開発 (AIDD):** 複数のAIエージェント（Claude Code, Codex, Antigravity）が協調して実装を行う。

---

## 2. Development Roadmap

本プロジェクトは段階的に機能を実装します。現在は **[Phase 1]** です。

### Phase 1: AI Proofing Assistant (Chrome Extension)
* **Goal:** 人間が書いたGoogle Docs記事を検収する際の工数を削減する。
* **Features:**
    * Google Docsを開くとSide Panelに拡張機能が起動。
    * 原文を読み取り、Gemini APIで校閲（誤字脱字、法務チェック、ハルシネーション検出）。
    * 指摘箇所と修正案をリスト表示。
    * 「修正」ボタンでGoogle Docsに反映（コメント挿入またはテキスト置換）。

### Phase 2: AI Writer Integration
* **Goal:** 記事の構成作成から執筆までをAIが担当し、Phase 1のUIで人間が最終確認を行う。
* **Features:**
    * キーワード・構成案に基づく記事生成ロジックの実装。
    * 生成された記事データ（原文＋自己チェックログ）をPhase 1のUIに流し込む。
    * **重要:** Phase 1のフロントエンド資産をそのまま利用するため、データ構造の互換性を維持する。

---

## 3. System Architecture

### Tech Stack
* **Frontend (Chrome Extension):**
    * React, Vite, TypeScript
    * UI Framework: Tailwind CSS, Shadcn/ui (推奨)
    * Platform: Chrome Extension Manifest V3 (Side Panel API)
* **Backend (API Server):**
    * Python (FastAPI)
    * AI Integration: LangChain, Google Gemini API
    * Docs Integration: Google Docs API
* **Infrastructure:**
    * Frontend: GitHub Pages or Local Load (for dev)
    * Backend: Cloud Run or Vercel (Python runtime)

### Data Flow (Phase 1)
1.  **Client (Extension):** Google Docsからテキストを取得 -> Backendへ送信。
2.  **Backend:** Gemini APIで校閲実行 -> 結果を共通JSONフォーマットに整形 -> Clientへ返却。
3.  **Client (Extension):** 結果を表示。ユーザー操作（修正）トリガー -> Google Docs APIを実行して反映。

---

## 4. Branch Strategy & AI Agent Roles

GitHubを中心とした非エンジニア主導の開発フローを採用します。

### Branches
* `main`: 安定稼働版（Production）。
* `develop`: 開発統合ブランチ（Staging）。各FeatureブランチはここにPRを送る。
* `feature/extension-ui`: フロントエンド・UI実装用。
* `feature/backend-logic`: バックエンド・AIロジック実装用。

### Assignments for AI Agents

#### 🤖 Claude Code / Codex
* **Assigned Branch:** `feature/extension-ui`
* **Responsibilities:**
    * Manifest V3に基づいたChrome拡張機能のボイラープレート作成。
    * `sidePanel` 権限の設定とReact環境の構築。
    * Google Docsと違和感のないUIデザイン（Tailwind CSS使用）。
    * **制約:** ロジック（AI処理）は含めず、APIから受け取ったJSONを表示することに徹する。モックデータを使ってUIを完成させること。

#### 🤖 Antigravity (Google IDE Agent)
* **Assigned Branch:** `feature/backend-logic`
* **Responsibilities:**
    * Python (FastAPI) 環境の構築。
    * Google Gemini APIを用いた校閲プロンプトの設計・実装。
    * Google Docs APIの認証周りと、ドキュメント操作（テキスト取得、コメント挿入）の実装。
    * **制約:** Phase 1とPhase 2で共通利用できる「Data Schema」に従ってレスポンスを返すこと。

---

## 5. Shared Data Schema (JSON)

Phase 1(校閲)とPhase 2(自動執筆)の互換性を保つため、フロントエンドとバックエンド間の通信は以下のフォーマットを厳守してください。

```json
{
  "document_id": "string",
  "items": [
    {
      "id": "uuid",
      "original_text": "指摘対象の原文テキスト",
      "suggested_text": "修正案のテキスト",
      "category": "TYPO" | "LEGAL" | "HALLUCINATION" | "STYLE",
      "reason": "AIによる指摘理由",
      "location_index": {
        "start_index": 100,
        "end_index": 115
      },
      "status": "PENDING" | "FIXED" | "IGNORED"
    }
  ]
}
