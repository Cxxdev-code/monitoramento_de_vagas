import os
import discord
from discord.ext import commands, tasks

from html_parser import get_projects_html, get_html_parser
from database import save_projects, read_data
from dotenv import load_dotenv

# ============================
# CONFIGURAÇÃO
# ============================
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

ids_enviados = set()

# ============================
# FUNÇÕES DO SISTEMA
# ============================

def atualizar_projetos():
    print("🔄 Rodando Selenium + Parser...")
    html_projects = get_projects_html()
    projects = get_html_parser(html_projects)
    save_projects(projects)
    print("✅ Banco atualizado")


def buscar_projetos():
    return read_data()

# ============================
# EVENTOS
# ============================

@bot.event
async def on_ready():
    print(f"🤖 Bot conectado como {bot.user}")
    monitorar_novos.start()

# ============================
# COMANDOS
# ============================

@bot.command()
async def atualizar(ctx):
    await ctx.send("🔄 Buscando novos projetos...")
    atualizar_projetos()
    await ctx.send("✅ Projetos atualizados!")


@bot.command()
async def projetos(ctx):
    projetos = buscar_projetos()

    if not projetos:
        await ctx.send("❌ Nenhum projeto encontrado.")
        return

    mensagem = ""
    for p in projetos[:5]:  # evita flood
        mensagem += (
            f"📌 **{p[5]}**\n"
            f"💼 {p[2]} | {p[4]}\n"
            f"🕒 {p[3]}\n"
            f"🔗 {p[7]}\n\n"
        )

    await ctx.send(mensagem)

# ============================
# ALERTAS AUTOMÁTICOS
# ============================

@tasks.loop(minutes=5)
async def monitorar_novos():
    canal = bot.get_channel(DISCORD_CHANNEL_ID)
    projetos = buscar_projetos()

    for p in projetos:
        if p[1] not in ids_enviados:
            ids_enviados.add(p[1])
            await canal.send(
                f"🔥 **Novo projeto encontrado!**\n\n"
                f"📌 {p[5]}\n"
                f"💼 {p[2]} | {p[4]}\n"
                f"🔗 {p[7]}"
            )

# ============================
# START
# ============================

bot.run(DISCORD_TOKEN)
