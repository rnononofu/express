from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.templates import templates

router = APIRouter()


@router.get("/sample", response_class=HTMLResponse)
def sample(request: Request):
    return templates.TemplateResponse(request, "sample/index.html")
