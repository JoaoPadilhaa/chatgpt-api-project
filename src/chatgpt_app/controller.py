from chatgpt_app.services import ChatService, OpenAIServiceError
from chatgpt_app.validators import validar_prompt


class ChatController:
    def __init__(self, service: ChatService, debug: bool = False) -> None:
        self._service = service
        self._debug = debug

    def processar(self, prompt: str) -> str:
        if not validar_prompt(prompt):
            return "Digite uma pergunta válida."

        try:
            return self._service.obter_resposta(prompt.strip())
        except OpenAIServiceError as exc:
            if self._debug:
                return f"Não foi possível obter resposta da OpenAI. Detalhes: {exc}"
            return "Não foi possível obter resposta da OpenAI."
