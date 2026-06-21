import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    api_key: str
    model: str = "gpt-5.5"


def carregar_configuracao() -> AppConfig:
    return AppConfig(
        api_key=os.getenv("OPENAI_API_KEY", ""),
        model=os.getenv("OPENAI_MODEL", "gpt-5.5"),
    )

