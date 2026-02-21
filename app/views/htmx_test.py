from datetime import datetime

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse

from app.templates import templates

router = APIRouter(prefix="/htmx-test")

SAMPLE_ITEMS = [
    {"id": 0, "name": "アイテム A"},
    {"id": 1, "name": "アイテム B"},
    {"id": 2, "name": "アイテム C"},
    {"id": 3, "name": "アイテム D"},
]


@router.get("", response_class=HTMLResponse)
def htmx_test(request: Request):
    return templates.TemplateResponse(request, "htmx_test/index.html")


@router.get("/time", response_class=HTMLResponse)
def time(request: Request):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return templates.TemplateResponse(
        request, "htmx_test/partials/time.html", {"now": now}
    )


@router.post("/greet", response_class=HTMLResponse)
def greet(request: Request, name: str = Form("")):
    ctx = {"error": "名前を入力してください"} if not name.strip() else {"name": name}
    return templates.TemplateResponse(request, "htmx_test/partials/greet.html", ctx)


@router.get("/items", response_class=HTMLResponse)
def items(request: Request):
    return templates.TemplateResponse(
        request, "htmx_test/partials/items.html", {"items": SAMPLE_ITEMS}
    )


@router.delete("/items/{item_id}", response_class=HTMLResponse)
def delete_item(item_id: int):
    return ""
