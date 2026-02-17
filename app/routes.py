from fastapi import APIRouter

from app.views.api import router as api_router
from app.views.home import router as home_router
from app.views.htmx_test import router as htmx_test_router
from app.views.sample import router as sample_router

router = APIRouter()

router.include_router(home_router)
router.include_router(htmx_test_router)
router.include_router(sample_router)
router.include_router(api_router)
