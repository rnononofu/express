# Express - 開発ガイド

## 概要
社内配布用 Windows 常駐アプリ。FastAPI + htmx + Tailwind CSS (DaisyUI) で構築。

## 技術スタック

| 領域 | 技術 |
|------|------|
| 言語 | Python 3.12 |
| パッケージ管理 | uv |
| Web サーバー | FastAPI + Uvicorn |
| テンプレート | Jinja2 |
| フロントエンド | htmx (サーバー駆動 UI) |
| スタイリング | Tailwind CSS v4 + DaisyUI |
| CSS ビルド | @tailwindcss/cli (bun 経由) |
| リンター | ruff |
| タスクランナー | taskipy |

## コマンド

```bash
uv run task dev        # 開発サーバー + CSS 監視 (同時起動)
uv run task server     # uvicorn のみ (--reload, 0.0.0.0:8000)
uv run task css_watch  # Tailwind CSS 監視のみ
uv run task css_build  # Tailwind CSS 本番ビルド (--minify)
```

## プロジェクト構成

```
app/
├── main.py              # サーバー設定 (FastAPI, middleware, static)
├── routes.py            # ルーターインデックス (include_router のみ)
├── templates.py         # Jinja2Templates 共有インスタンス
├── views/               # ビジネスロジック (Python)
│   ├── home.py          # /
│   ├── htmx_test.py     # /htmx-test
│   ├── sample.py        # /sample
│   └── api.py           # /api/*
├── templates/           # テンプレート (HTML)
│   ├── base.html        # ベーステンプレート
│   ├── home/
│   │   └── index.html
│   ├── htmx_test/
│   │   ├── index.html
│   │   └── partials/    # htmx パーシャル
│   │       ├── time.html
│   │       ├── greet.html
│   │       └── items.html
│   └── sample/
│       └── index.html
└── static/
    └── css/
        └── style.css    # ビルド出力 (.gitignore 対象)

assets/
├── css/
│   └── tailwind.css     # Tailwind ソース (@source, @plugin 定義)
├── package.json
└── node_modules/        # .gitignore 対象
```

## 開発規約

### 新しいページを追加する手順

1. `app/views/xxx.py` を作成 — `APIRouter` でルート定義、ロジックのみ書く
2. `app/templates/xxx/` を作成 — HTML テンプレートを配置
3. `app/routes.py` に import + `router.include_router()` を1行追加
4. `app/templates/base.html` のナビバーにリンク追加

### ビジネスロジックとテンプレートの分離

- `app/views/` — Python ロジックのみ。HTML を直書きしない
- `app/templates/` — HTML のみ。ビュー名と同じディレクトリ名で対応付け
- htmx パーシャルレスポンスも `templates/xxx/partials/` にテンプレートとして配置

### routes.py の役割

ルーターのインデックス専用。ルート定義は書かない。

```python
from app.views.xxx import router as xxx_router
router.include_router(xxx_router)
```

### テンプレート参照

`app/templates.py` の共有インスタンスを使う:

```python
from app.templates import templates
templates.TemplateResponse(request, "xxx/index.html", {"key": "value"})
```

### Tailwind CSS

- ソース: `assets/css/tailwind.css`
- `@source "../../app/templates"` で `app/templates/` 以下を再帰スキャン
- HTML を編集すると `--watch` モードで自動ビルドされる
- ビルド出力 `app/static/css/style.css` は gitignore 対象
