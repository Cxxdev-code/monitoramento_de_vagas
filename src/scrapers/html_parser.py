from bs4 import BeautifulSoup
from src.scrapers.browser import get_html_browser
import re

    
    
    
def get_projects_html():
    result_html = get_html_browser()
    
    soup = BeautifulSoup(result_html, 'html.parser')

    all_projects = soup.find_all("li", class_=["with-flag", "result-item"])
    if all_projects:
        print('peguei o html cru')

    return all_projects


def results_scraping(db_projects):
    for project in db_projects:
        print("=" * 50)
        
        print(f"📂 Categoria : {project['categoria']}")
        print(f"📊 Nível     : {project['nivel']}")
        print(f"🗓️  Publicado : {project['publicado']}")
        print("-" * 50)
        print(f"📝 Título    : {project['titulo']}")
        print(f"📄 Descrição : {project['descriçao']}")
        print(f"🔗 Link      : {project['link']}")
        print("-" * 50)
        print(f"🆔 ID        : {project['project_id']}")
        print("=" * 50)
        print()
 
        
def get_html_parser(all_projects):
    lista_projetos = []
    
    for project in all_projects:
        
        
        dados = {
            'categoria': "N/A",
            'nivel': "N/A",
            'publicado': "N/A",
            'titulo': "N/A",
            'descriçao': "N/A",
            'link': "N/A",
            'ID': "N/A"
        }

        try:
            
            
            dados['ID'] = project.get('data-id', "N/A")
                 
            tags_info = project.find('p', class_='information')
            if tags_info:
                
                partes = [p.strip() for p in tags_info.get_text(separator="|").split('|') if p.strip()]
                if len(partes) >= 1: dados['categoria'] = partes[0]
                if len(partes) >= 2: dados['nivel'] = partes[1]
                
                
                tempo_tag = tags_info.find('b', class_='datetime')
                if tempo_tag:
                    dados['publicado'] = tempo_tag.get_text(strip=True)

            title_tag = project.find('h1', class_='title')
            if title_tag:
                a_tag = title_tag.find('a')
                if a_tag:
                    dados['titulo'] = a_tag.get_text(strip=True)
                    link_relativo = a_tag.get('href', '')
                    dados['link'] = f"https://www.99freelas.com.br{link_relativo}"

           
            desc_tag = project.find('div', class_='description')
            if desc_tag:
    
                dados['descriçao'] = desc_tag.get_text(strip=True).replace('… Expandir', '')

        except Exception as e:
            print(f"Erro ao processar projeto {dados['ID']}: {e}")

        lista_projetos.append(dados)

    print(f'Dicionário criado com {len(lista_projetos)} projetos.')
    return lista_projetos
    

def published_to_minutes(texto):
    if not texto:
        return float('inf')

    texto = texto.lower().strip()

    if 'agora' in texto:
        return 0

    match = re.search(r'(\d+)', texto)
    if not match:
        return float('inf')

    valor = int(match.group(1))

    if 'minuto' in texto:
        return valor
    if 'hora' in texto:
        return valor * 60
    if 'dia' in texto:
        return valor * 1440
    if 'semana' in texto:
        return valor * 10080

    return float('inf')
  
if __name__  == "__main__":
    all_projects = get_projects_html()
    project_parser = get_html_parser(all_projects)
    results_scraping(project_parser)
    
    

    
    


