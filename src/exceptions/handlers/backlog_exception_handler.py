from fastapi.responses import JSONResponse
from typing import Callable
from urllib.request import Request

from exceptions.backlog_exceptions import BacklogException


class BacklogExceptionHandler:
    
    def create_exception_handler(status_code: int) -> Callable[[Request, BacklogException], JSONResponse]:
        detail = {}
    
        async def exception_handler(_: Request, exc: BacklogException) -> JSONResponse:
            if exc.message:
                detail["message"] = exc.message
        
            if exc.name:
                detail["message"] = f"{detail['message']} [{exc.name}]"
        
            return JSONResponse(status_code=status_code, content={"detail": detail["message"]})
        
        return exception_handler