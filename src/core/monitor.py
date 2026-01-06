from src.scrapers.html_parser import get_html_parser, get_projects_html
from src.database.database import save_to_db, read_data

def run_scraper():
    print("🔎 Coletando dados...")
    html = get_projects_html()
    projects = get_html_parser(html)

    save_to_db(projects)
    return read_data()