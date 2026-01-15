import discord
import os
from dotenv import load_dotenv
import asyncio
from collections import deque
from discord.ext import commands 

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
TEMPO_EXPIRACAO = 85800  


intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

queue = deque()

@bot.event
async def on_ready():
    print(f"🤖 Bot conectado como {bot.user}")
    
    bot.loop.create_task(process_queue())


@bot.command(name="limpar")
async def limpar(ctx, quantidade: int = 100):
    
    if ctx.channel.id == CHANNEL_ID:
        deleted = await ctx.channel.purge(limit=quantidade)
       
        confirmacao = await ctx.send(f"🧹 Faxina concluída! {len(deleted)} mensagens removidas.")
        await asyncio.sleep(5)
        await confirmacao.delete()

async def process_queue():
    await bot.wait_until_ready()
    
    while True:
        if queue:
            channel = bot.get_channel(CHANNEL_ID)
            if channel:
                dados = queue.popleft()
                
                cor_vaga = discord.Color.blue() 
                nivel = dados.get('nivel', '').lower()

                if 'iniciante' in nivel:
                    cor_vaga = discord.Color.green()
                elif 'intermediário' in nivel or 'intermediario' in nivel:
                    cor_vaga = discord.Color.gold() 
                elif 'especialista' in nivel:
                    cor_vaga = discord.Color.red()

               
                embed = discord.Embed(
                    title=f"🤖 {dados.get('titulo', 'Sem título')}",
                    url=dados.get('link'),
                    description=f"```text\n{dados.get('descriçao', '')[:250]}...```",
                    color=cor_vaga,
                    timestamp=discord.utils.utcnow()
                )
                
                embed.add_field(name="💼 Categoria", value=f"**{dados.get('categoria', 'N/A')}**", inline=True)
                embed.add_field(name="📊 Nível", value=f"`{dados.get('nivel', 'N/A')}`", inline=True)
                timestamp_now = int(discord.utils.utcnow().timestamp())
                embed.add_field(name="🕒 Publicado", value=f"<t:{timestamp_now}:R>", inline=True)
                embed.set_footer(text=f"99Freelas Bot • ID: {dados.get('ID')}")
                
                try:
                   
                    await channel.send(embed=embed, delete_after=TEMPO_EXPIRACAO)
                except Exception as e:
                    print(f"Erro ao enviar embed: {e}")
                
                await asyncio.sleep(2)
        else:
            await asyncio.sleep(1)

def send_message(project_dict):
    queue.append(project_dict)

def start_bot():
    bot.run(TOKEN)