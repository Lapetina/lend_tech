# Lend Tech

Este repositório foi criado para consultar as condições climáticas dos próximos 5 dias para algumas cidades específicas e sugerir as roupas mais adequadas de acordo com a previsão.

## Cidades Suportadas

Aqui estão as cidades suportadas e seus respectivos códigos (`city_code`):

- Santiago: 60449
- São Paulo: 45881
- New York: 349727
- Beijing: 101924
- Cairo: 127164

Essas informações são obtidas da [AccuWeather](https://developer.accuweather.com/accuweather-forecast-api/apis).

## Funcionalidade

A API verifica as condições climáticas e recomenda roupas adequadas para cada dia com base na previsão do tempo.

## Como Rodar a API Localmente

Siga os passos abaixo para configurar e rodar a API localmente:

### 1. Configurar o Ambiente Python

1. Caso não tenha o Python instalado na sua máquina ou não tenha a versão desejada:
   - Instale o `pyenv`, se ainda não estiver instalado. 
   - Instale a versão do Python 3.10 ou posterior:
     ```sh
     pyenv install 3.10
     pyenv local 3.10
     ```
   - Instale o `poetry`, se ainda não estiver instalado. Siga a [documentação oficial](https://python-poetry.org/docs/).

### 2. Instalar Dependências

1. Crie o arquivo `.env` conforme o `template_env`.
2. No terminal, execute os seguintes comandos:
   ```sh
   env $(cat .env) poetry shell
   poetry install

### 3. Subir o servidor
1. No terminal, execute o seguinte comando para iniciar o servidor:
   ```sh
   python app/http_server.py

### 4. Realizar uma Requisição

1. Para realizar uma requisição local, utilize o seguinte comando `curl`:

- Request:
  ```sh
  curl --location 'localhost:8000/v1/climate/check-conditions?city_code=45881'

- Response esperado:
    ```json
    {
  "forecasts": [
  {
    "date": "2024-06-24",
    "clothes": ["Shorts"]
  },
  {
    "date": "2024-06-25",
    "clothes": ["Fleece", "Short Sleeves", "Rain Coat"]
  },
  {
    "date": "2024-06-26",
    "clothes": ["Shorts"]
  },
  {
    "date": "2024-06-27",
    "clothes": ["Fleece", "Short Sleeves", "Rain Coat"]
  },
  {
    "date": "2024-06-28",
    "clothes": ["Shorts"]
    }
   ]
  }
  ```
### Código Fonte

    lend_tech/
    ├── app/
    │   ├── __init__.py
    │   ├── http_server.py
    │   └── routers/
    │       ├── __init__.py
    │       └── climate_condition_router.py
    ├── .venv/
    ├── .env
    ├── template_env
    └── README.m

### Links
[Documentação da AccuWeather](https://developer.accuweather.com/accuweather-forecast-api/apis)