import openai
import time

# Configure a API key da OpenAI
openai.api_key = "API_KEY"

# Define a pergunta a ser enviada
prompt = "Diga isso é um teste" #Sua pergunta aqui

# Define as configurações do modelo
completions_args = {
    "temperature": 0.7,
    "max_tokens": 50,
    "n": 1,
    "stop": "\n"
}

# Chama a API do OpenAI para gerar uma resposta
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    **completions_args
)

# Verifica se a resposta está completa
while response["choices"][0]["text"].endswith((".", "?", "!")) == False:
    # A resposta não está completa, aguarda um tempo e faz outra chamada à API para continuar a resposta
    time.sleep(0.3)
    response = openai.Completion.create(
        engine="davinci",
        prompt=response["choices"][0]["text"],
        **completions_args
    )
# A resposta está completa, exibe a resposta
print(response["choices"][0]["text"])
