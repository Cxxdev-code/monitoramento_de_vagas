from bs4 import BeautifulSoup
from src.scrapers.browser import get_html_browser


    
    
    
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
        print(f"🆔 ID        : {project['ID']}")
        print("=" * 50)
        print()
 
        
def get_html_parser(all_projects):
    lista_projetos = []
    
    for project in all_projects:
        # Inicializa com N/A para garantir que o dicionário sempre tenha as chaves
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
            # 1. Extrair ID diretamente do atributo data-id (muito mais seguro)
            dados['ID'] = project.get('data-id', "N/A")

            # 2. Extrair Informações (Categoria, Nível, Publicado)
            tags_info = project.find('p', class_='information')
            if tags_info:
                # O separator "|" ajuda a dividir as strings sem perder o contexto
                partes = [p.strip() for p in tags_info.get_text(separator="|").split('|') if p.strip()]
                if len(partes) >= 1: dados['categoria'] = partes[0]
                if len(partes) >= 2: dados['nivel'] = partes[1]
                
                # O tempo publicado geralmente está dentro de um <b> com classe datetime
                tempo_tag = tags_info.find('b', class_='datetime')
                if tempo_tag:
                    dados['publicado'] = tempo_tag.get_text(strip=True)

            # 3. Título e Link
            title_tag = project.find('h1', class_='title')
            if title_tag:
                a_tag = title_tag.find('a')
                if a_tag:
                    dados['titulo'] = a_tag.get_text(strip=True)
                    link_relativo = a_tag.get('href', '')
                    dados['link'] = f"https://www.99freelas.com.br{link_relativo}"

            # 4. Descrição (usando find direto na classe específica)
            desc_tag = project.find('div', class_='description')
            if desc_tag:
                # Removemos o texto de "Expandir" se houver
                dados['descriçao'] = desc_tag.get_text(strip=True).replace('… Expandir', '')

        except Exception as e:
            print(f"Erro ao processar projeto {dados['ID']}: {e}")

        lista_projetos.append(dados)

    print(f'Dicionário criado com {len(lista_projetos)} projetos.')
    return lista_projetos
    
    
if __name__  == "__main__":
    all_projects = get_projects_html()
    project_parser = get_html_parser(all_projects)
    results_scraping(project_parser)
    
    

    
    


