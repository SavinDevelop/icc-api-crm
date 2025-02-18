import jwt
from typing import Any
from result import Result

from core.settings import SECRET_KEY, ALGORITHM_ENCRYPTION_TOKEN

def encode_token(body_for_encode: dict[str, Any]) -> str:
    return jwt.encode(body_for_encode, SECRET_KEY, algorithm=ALGORITHM_ENCRYPTION_TOKEN)

def decode_token(token_for_decode: str) -> Result[dict[str, Any], str]:
    try:
        decoded = jwt.decode(token_for_decode, SECRET_KEY, algorithms=[ALGORITHM_ENCRYPTION_TOKEN])
        return Result.Ok(decoded)
    except jwt.PyJWTError as e:
        return Result.Err(str(e))
