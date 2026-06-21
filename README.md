# Projeto ChatGPT Console

Aplicação acadêmica simples em Python que recebe uma pergunta pelo terminal,
envia o texto para a API da OpenAI e exibe a resposta ao usuário.

## Objetivo

Demonstrar um fluxo básico de desenvolvimento com:

- Python 3.12+
- Integração com a API oficial da OpenAI
- Testes automatizados com pytest
- Organização seguindo Clean Code e princípios SOLID
- Integração contínua com GitHub Actions

## Estrutura

```text
.
├── .github/workflows/ci.yml
├── src/chatgpt_app/
│   ├── cli.py
│   ├── config.py
│   ├── controller.py
│   ├── services.py
│   └── validators.py
├── tests/
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Como executar

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a chave da API:

```powershell
$env:OPENAI_API_KEY="sua-chave-aqui"
```

Opcionalmente, configure outro modelo:

```powershell
$env:OPENAI_MODEL="gpt-5.4-mini"
```

Para ver detalhes técnicos caso a API retorne erro:

```powershell
$env:CHATGPT_DEBUG="1"
```

Execute a aplicação:

```bash
python main.py
```

## Como usar

Digite uma pergunta no terminal e pressione Enter.

Exemplo:

```text
Pergunta: O que é programação orientada a objetos?
```

Para sair:

```text
sair
```

## Testes

Execute:

```bash
pytest
```

Os testes não fazem chamadas reais para a API da OpenAI. Eles usam objetos falsos
para simular as respostas e erros da integração externa.

## Variáveis de ambiente

| Variável | Obrigatória | Descrição |
| --- | --- | --- |
| `OPENAI_API_KEY` | Sim | Chave da API da OpenAI |
| `OPENAI_MODEL` | Não | Modelo usado pela aplicação. Padrão: `gpt-5.4-mini` |
| `CHATGPT_DEBUG` | Não | Mostra detalhes técnicos de erro quando definido como `1` |

## GitHub Actions

O workflow `.github/workflows/ci.yml` executa automaticamente:

1. Checkout do código
2. Configuração do Python 3.12
3. Instalação das dependências
4. Execução do `pytest`

Se algum teste falhar, o pipeline também falha.
