from chatgpt_app.config import carregar_configuracao
from chatgpt_app.controller import ChatController
from chatgpt_app.services import OpenAIChatService


def criar_controller() -> ChatController:
    config = carregar_configuracao()
    if not config.api_key:
        raise RuntimeError("Configure a variável de ambiente OPENAI_API_KEY.")

    service = OpenAIChatService(api_key=config.api_key, model=config.model)
    return ChatController(service)


def executar() -> None:
    try:
        controller = criar_controller()
    except RuntimeError as exc:
        print(exc)
        return

    print("ChatGPT Console")
    print("Digite 'sair' para encerrar.")

    while True:
        prompt = input("\nPergunta: ")
        if prompt.strip().lower() == "sair":
            print("Encerrando...")
            break

        resposta = controller.processar(prompt)
        print(f"\nResposta:\n{resposta}")
