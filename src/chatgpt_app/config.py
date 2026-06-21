import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    api_key: str
    model: str = "gpt-5.4-mini"
    debug: bool = False


def carregar_configuracao() -> AppConfig:
    return AppConfig(
        api_key=os.getenv("OPENAI_API_KEY", ""),
        model=os.getenv("OPENAI_MODEL", "gpt-5.4-mini"),
        debug=os.getenv("CHATGPT_DEBUG", "").lower() in {"1", "true", "sim", "yes"},
    )
