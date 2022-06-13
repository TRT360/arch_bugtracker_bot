import sys
from typing import Any

from pydantic import BaseModel, Field, validator


class TelegramConfig(BaseModel):
    ...


class SystemConfig(BaseModel):
    env: str


class ParserConfig(BaseModel):
    ...


class LoggingConfig(BaseModel):
    sink: Any
    format_: str = Field(alias='format')
    level: str

    @validator('sink')
    def validate_sink(cls, sink: Any) -> Any:
        match sink:
            case sink if 'stdout' in sink:
                return sys.stdout
            case sink if 'stderr' in sink:
                return sys.stderr
            case _:
                pass

        return sink
