import sqlite3

DB_FILE = r'C:\Users\Caina\Documents\selenium\data\freelas_projects.db'

NAME_TABLE = 'projetos'

def dell_banc():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute(f'DELETE FROM {NAME_TABLE};')
    
    
    conn.commit()
    conn.close()
    


def create_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS projetos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id TEXT UNIQUE,
        categoria TEXT,
        publicado TEXT,
        nivel TEXT,
        titulo TEXT,
        descriçao TEXT,
        link TEXT)''')
    
    conn.commit()
    conn.close()
    
def save_projects(list_projects):
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    
    
    for project in list_projects:
        
        project_id = project['ID']
        categoria = project['categoria']
        publicado = project['publicado']
        nivel = project['nivel']
        titulo = project['titulo']
        descriçao = project['descriçao']
        link = project['link']
        
        cursor.execute(f'''INSERT OR IGNORE INTO {NAME_TABLE}
                    (project_id, categoria, publicado, nivel, titulo, descriçao, link)
                    values
                    (?,?,?,?,?,?,?)''',
                    (project_id, categoria, publicado, nivel, titulo, descriçao, link))
        print('projeto posto no banco de dados')
        
        
    conn.commit()
    conn.close()


def read_data():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()   
    
    cursor.execute(f'''SELECT * FROM {NAME_TABLE}''')
    all_projects = cursor.fetchall()
    return all_projects


if __name__ == '__main__':
    
    unc =  str(input(" esxluir bnc: "))
    if unc == "s":
        dell_banc()
    create_db()
    
            
    