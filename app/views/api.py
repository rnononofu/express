from fastapi import APIRouter

router = APIRouter(prefix="/api")


@router.get("/data")
def read_data():
    return {"message": "Hello from FastAPI"}
