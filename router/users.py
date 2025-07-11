from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth.security import verify_token

router = APIRouter()
bearer_scheme = HTTPBearer()


@router.get("/me", tags=["Users"])
def get_me(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user": payload.get("sub")}
