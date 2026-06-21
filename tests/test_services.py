from types import SimpleNamespace

from chatgpt_app.services import OpenAIChatService, OpenAIServiceError


class FakeResponses:
    def __init__(self, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error

    def create(self, model: str, input: str):
        if self._error:
            raise self._error
        return self._response


class FakeClient:
    def __init__(self, response=None, error: Exception | None = None) -> None:
        self.responses = FakeResponses(response=response, error=error)


def test_obter_resposta_retorna_texto_simulado() -> None:
    response = SimpleNamespace(output_text="Olá usuário")
    service = OpenAIChatService(
        api_key="fake-key",
        model="fake-model",
        client=FakeClient(response=response),
    )

    resposta = service.obter_resposta("Olá")

    assert resposta == "Olá usuário"


def test_obter_resposta_transforma_erro_da_api() -> None:
    service = OpenAIChatService(
        api_key="fake-key",
        model="fake-model",
        client=FakeClient(error=RuntimeError("api fora do ar")),
    )

    try:
        service.obter_resposta("Olá")
    except OpenAIServiceError:
        assert True
    else:
        assert False, "OpenAIServiceError deveria ser lançado"

