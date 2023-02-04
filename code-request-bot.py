import discord
import requests

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
def get_answer(question):
    api_key = "API_OPENAI"
    api_url = "https://api.openai.com/v1/engines/davinci/jobs"
    request_content = {
     "prompt": question,
     "max_tokens": 2048,
    }

    response = requests.post(api_url, headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }, json=request_content)

    if response.status_code == 200:
        response_text = response.json()["choices"][0]["text"]
        print(response_text)
    else:
        print("A requisição falhou com o status code:", response.status_code)


@client.event
async def on_message(message):
    if message.content.startswith('!gpt3'):
        print('Li sua mensagem!')
        
        question = message.content[6:]
        
        answer = get_answer(question)
        await message.channel.send(answer)

client.run('API_BOT')