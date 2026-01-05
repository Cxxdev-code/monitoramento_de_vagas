
from src.html_parser import get_html_parser, get_projects_html, results_scraping
from src.database import save_projects, read_data

if __name__ == "__main__":
    all_projects = get_projects_html()
    dicionario_projects = get_html_parser(all_projects)
    save_projects(dicionario_projects)
    db_projects = read_data()
    results_scraping(db_projects)