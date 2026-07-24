from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("")
def health():
    return {
        "status": "healthy",
        "service": "AI Fire Engineering Platform"
    }

@router.get("/version")
def version():
    return {
        "version": "0.1.0",
        "environment": "development"
    }