from chatgpt_app.controller import ChatController
from chatgpt_app.services import OpenAIServiceError


class FakeService:
    def __init__(self, resposta: str = "Resposta simulada", deve_falhar: bool = False) -> None:
        self.resposta = resposta
        self.deve_falhar = deve_falhar
        self.prompt_recebido = ""

    def obter_resposta(self, prompt: str) -> str:
        self.prompt_recebido = prompt
        if self.deve_falhar:
            raise OpenAIServiceError("falha")
        return self.resposta


def test_controller_nao_envia_prompt_vazio() -> None:
    service = FakeService()
    controller = ChatController(service)

    resposta = controller.processar("   ")

    assert resposta == "Digite uma pergunta válida."
    assert service.prompt_recebido == ""


def test_controller_retorna_mensagem_amigavel_em_erro() -> None:
    controller = ChatController(FakeService(deve_falhar=True))

    resposta = controller.processar("Explique Python")

    assert resposta == "Não foi possível obter resposta da OpenAI."


def test_controller_exibe_detalhes_quando_debug_ativo() -> None:
    controller = ChatController(FakeService(deve_falhar=True), debug=True)

    resposta = controller.processar("Explique Python")

    assert "Não foi possível obter resposta da OpenAI." in resposta
    assert "falha" in resposta
