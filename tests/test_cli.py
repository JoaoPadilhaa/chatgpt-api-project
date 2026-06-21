from chatgpt_app.cli import criar_controller


def test_criar_controller_exige_api_key(monkeypatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    try:
        criar_controller()
    except RuntimeError as exc:
        assert str(exc) == "Configure a variável de ambiente OPENAI_API_KEY."
    else:
        assert False, "RuntimeError deveria ser lançado sem OPENAI_API_KEY"

