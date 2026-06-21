from chatgpt_app.validators import validar_prompt


def test_validar_prompt_rejeita_texto_vazio() -> None:
    assert validar_prompt("") is False
    assert validar_prompt("   ") is False


def test_validar_prompt_aceita_texto_preenchido() -> None:
    assert validar_prompt("O que é orientação a objetos?") is True

