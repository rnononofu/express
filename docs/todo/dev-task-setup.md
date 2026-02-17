# 開発タスクランナーのセットアップ

## 完了日: 2026-02-18

## 概要
`uv run task dev` で FastAPI (uvicorn) と Tailwind CSS 監視ビルドを同時起動できるようにした。

## 変更内容

### 1. taskipy 導入 (`pyproject.toml`)
- `taskipy` を依存関係に追加
- 以下のタスクを定義:
  - `dev` - uvicorn + Tailwind CSS watch を同時起動
  - `server` - uvicorn のみ (`--reload` 付き、`0.0.0.0:8000`)
  - `css_watch` - Tailwind CSS 監視モード
  - `css_build` - Tailwind CSS 本番ビルド (`--minify`)

### 2. FastAPI アプリ更新 (`app/main.py`)
- `StaticFiles` で `/static` パスに静的ファイル配信を追加
- `Jinja2Templates` でテンプレートエンジンを設定
- `/` ルートを追加 (`index.html` を返す)

### 3. テンプレート作成
- `app/templates/base.html` - ベーステンプレート (Tailwind CSS + htmx 読み込み)
- `app/templates/index.html` - トップページ

### 4. Tailwind CSS 設定 (`assets/css/tailwind.css`)
- `@source "../../app/templates"` を追加してテンプレートディレクトリをスキャン対象に設定

### 5. ビルド出力ディレクトリ
- `app/static/css/` を作成 (Tailwind CSS のビルド出力先)
- `.gitignore` に `app/static/css/style.css` を追加

## 利用方法
```bash
uv run task dev        # 開発サーバー + CSS監視 (同時起動)
uv run task server     # uvicorn のみ
uv run task css_watch  # Tailwind CSS 監視のみ
uv run task css_build  # Tailwind CSS 本番ビルド
```
