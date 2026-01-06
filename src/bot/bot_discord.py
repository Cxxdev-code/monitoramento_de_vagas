import discord
import os
from dotenv import load_dotenv
import asyncio
from collections import deque

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

bot_loop = None
queue = deque()

@client.event
async def on_ready():
    global bot_loop
    bot_loop = asyncio.get_running_loop()
    print(f"🤖 Bot conectado como {client.user}")
    client.loop.create_task(process_queue())

async def process_queue():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    
    while True:
        if queue:
            dados = queue.popleft()
            
           
            embed = discord.Embed(
                title=f"📌 {dados.get('titulo', 'Sem título')}",
                url=dados.get('link'),
                description=f"{dados.get('descriçao', '')[:300]}...",
                color=discord.Color.blue()
            )
            
            embed.add_field(name="💼 Categoria", value=dados.get('categoria', 'N/A'), inline=True)
            embed.add_field(name="📊 Nível", value=dados.get('nivel', 'N/A'), inline=True)
            embed.add_field(name="🕒 Publicado", value=dados.get('publicado', 'N/A'), inline=False)
            embed.set_footer(text=f"ID: {dados.get('ID')}")
            
            try:
                await channel.send(embed=embed)
            except Exception as e:
                print(f"Erro ao enviar embed: {e}")
                
            await asyncio.sleep(2)
        else:
            await asyncio.sleep(1)

def send_message(project_dict):
   
    queue.append(project_dict)

def start_bot():
    client.run(TOKEN)