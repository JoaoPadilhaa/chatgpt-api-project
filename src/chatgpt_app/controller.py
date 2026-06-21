from chatgpt_app.services import ChatService, OpenAIServiceError
from chatgpt_app.validators import validar_prompt


class ChatController:
    def __init__(self, service: ChatService) -> None:
        self._service = service

    def processar(self, prompt: str) -> str:
        if not validar_prompt(prompt):
            return "Digite uma pergunta válida."

        try:
            return self._service.obter_resposta(prompt.strip())
        except OpenAIServiceError:
            return "Não foi possível obter resposta da OpenAI."

