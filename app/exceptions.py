from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


class HTTPCustomException(HTTPException):
    pass


def my_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})