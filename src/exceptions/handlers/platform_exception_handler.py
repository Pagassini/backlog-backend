from typing import Callable
from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.platform_exceptions import PlatformException


class PlatformExceptionHandler:
    
    def create_exception_handler(status_code: int) -> Callable[[Request, PlatformException], JSONResponse]:
        detail = {}
    
        async def exception_handler(_: Request, exc: PlatformException) -> JSONResponse:
            if exc.message:
                detail["message"] = exc.message
        
            if exc.name:
                detail["message"] = f"{detail['message']} [{exc.name}]"
                    
            return JSONResponse(status_code=status_code, content={"detail": detail["message"]})
    
        return exception_handler