from bs4 import BeautifulSoup
from src.scraper import get_html_browser


    
    
    
def get_projects_html():
    result_html = get_html_browser()
    
    soup = BeautifulSoup(result_html, 'html.parser')

    all_projects = soup.find_all("li", class_="with-flag result-item")
    if all_projects:
        print('peguei o html cru')

    return all_projects


def results_scraping(db_projects):
    
    for project in db_projects:
        print("=" * 50)
        print(f"📂 Categoria : {project[2]}")
        print(f"📊 Nível     : {project[4]}")
        print(f"🗓️  Publicado : {project[3]}")
        print("-" * 50)
        print(f"📝 Título    : {project[5]}")
        print(f"📄 Descrição : {project[6]}")
        print(f"🔗 Link      : {project[7]}")
        print("-" * 50)
        print(f"🆔 ID        : {project[1]}")
        print("=" * 50)
        print() 

 
        
def get_html_parser(all_projects):
    
    dicionario_ = []
    
    
    for project in all_projects:
        category_ = nivel_ = publicado_ = title_ = link_ = description_ = project_id ="N/A"
        try:
            tags_ = project.find('p','item-text information')
            if tags_:
        
                info_ = tags_.get_text(separator="|").split('|')
                if len(info_[0]) > 0:
                    category_ = info_[0].strip()
                    
                if len(info_[1]) > 0:
                    nivel_ = info_[1].strip()
                    
        except Exception as e:
            print(f'erro 1{e}')
        try:
            tempo_tag = tags_.find('b', class_='datetime')
            publicado_ = tempo_tag.text.strip() if tempo_tag else "N/A"
                    
            title_tag = project.find('h1', class_='title')
            if title_tag:
                title_ = title_tag.text.strip()
                a_tag = title_tag.find('a') 
                if a_tag:
                    link_ = f"https://www.99freelas.com.br{a_tag['href']}"
                    project_id_full = a_tag['href'].split('/')[-1]
                    try:
 
                        slug = project_id_full.split('?')[0].split('/')[-1]
       
                        project_id = slug.split('-')[-1]
                    except:
                        project_id = "N/A"
            
            description_ = project.find('div', 'item-text description formatted-text').text.strip()
            
        except Exception as e:
            print(f'erro 2{e}')
        
        proj = {f'categoria': category_,
                'nivel': nivel_,
                'publicado': publicado_,
                'titulo': title_,
                'descriçao': description_,
                'link': link_,
                'ID': project_id}
        dicionario_.append(proj)
    if dicionario_:
        print('dicionario criado', len(dicionario_)) 
    return dicionario_
    
    
    
if __name__  == "__main__":
    all_projects = get_pojects_html()
    project_parser = get_html_parser(all_projects)
    results_scraping(project_parser)
    

    
    


