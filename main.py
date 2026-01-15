import time
import threading
from src.scrapers.html_parser import published_to_minutes
from src.core.monitor import run_scraper
from src.bot.bot_discord import start_bot, send_message


last_ids = set()

def scraping_loop():
    global last_ids
    print("🚀 Monitoramento de vagas iniciado...")

    while True:
        try:
          
            projects = run_scraper()

            if projects:
                print(f"🔎 Analisando {len(projects)} projetos...")
                projects.sort(
                 key=lambda p: published_to_minutes(p.get('publicado')),
                 reverse=True
                )
                
                for p in projects:
                    
                    project_id = p.get('project_id') or p.get('ID')

                    if project_id and project_id not in last_ids:
                        
                        last_ids.add(project_id)
                        
                        
                        p['ID'] = project_id
                        
                       
                        send_message(p)
                        print(f"✅ Nova vaga enviada para a fila: {p.get('titulo')}")
                    else:
                       
                        pass
            else:
                print("pocos ou nenhum projeto encontrado nesta rodada.")

        except Exception as e:
            print(f"❌ Erro crítico no loop de scraping: {e}")

        print("💤 Aguardando 5 minutos para a próxima coleta...")
        time.sleep(300)

if __name__ == "__main__":
    
    print("🤖 Iniciando thread do bot...")
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()

    
    time.sleep(10)

    
    scraping_loop()