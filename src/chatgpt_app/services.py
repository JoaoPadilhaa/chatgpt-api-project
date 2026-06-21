from typing import Any, Protocol


class OpenAIServiceError(Exception):
    """Erro esperado ao tentar obter uma resposta da OpenAI."""


class ChatService(Protocol):
    def obter_resposta(self, prompt: str) -> str:
        ...


class OpenAIChatService:
    def __init__(self, api_key: str, model: str, client: Any | None = None) -> None:
        self._model = model
        self._client = client or self._criar_cliente(api_key)

    def obter_resposta(self, prompt: str) -> str:
        try:
            response = self._client.responses.create(
                model=self._model,
                input=prompt,
            )
        except Exception as exc:
            raise OpenAIServiceError(f"Falha ao consultar a OpenAI: {exc}") from exc

        texto = self._extrair_texto(response)
        if not texto:
            raise OpenAIServiceError("A OpenAI retornou uma resposta vazia.")

        return texto

    def _extrair_texto(self, response: Any) -> str:
        output_text = getattr(response, "output_text", None)
        if output_text:
            return str(output_text).strip()

        partes: list[str] = []
        for item in getattr(response, "output", []) or []:
            for content in getattr(item, "content", []) or []:
                text = getattr(content, "text", "")
                if text:
                    partes.append(str(text))

        return "\n".join(partes).strip()

    def _criar_cliente(self, api_key: str) -> Any:
        from openai import OpenAI

        return OpenAI(api_key=api_key)
