import sqlite3

DB_FILE = r'C:\Users\Caina\Documents\Bot_freelas\data\freelas_projects.db'

NAME_TABLE = 'projetos'

def dell_banc():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute(f'DELETE FROM {NAME_TABLE};')
    
    
    conn.commit()
    conn.close()
    


def create_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {NAME_TABLE}(
        project_id TEXT PRIMARY KEY,
        categoria TEXT,
        publicado TEXT,
        nivel TEXT,
        titulo TEXT,
        descriçao TEXT,
        link TEXT)''')
    conn.commit()
    conn.close()
    
def save_to_db(list_projects):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    valid = []
    for project in list_projects:
        
        cursor.execute(f'''
            INSERT OR IGNORE INTO {NAME_TABLE}
            (project_id, categoria, publicado, nivel, titulo, descriçao, link)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (project['ID'], project['categoria'], project['publicado'], 
             project['nivel'], project['titulo'], project['descriçao'], project['link'])
        )
        cursor.execute(f"SELECT {project['ID']} FROM {NAME_TABLE}")
        valid.append(cursor.fetchone())
    
    conn.commit()
    conn.close()
    print(f"Processo finalizado: {len(valid)} novos projetos processados.")
    valid.clear()


def read_data():
    conn = sqlite3.connect(DB_FILE)
    
  
    conn.row_factory = sqlite3.Row 
    
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {NAME_TABLE}")
    
    rows = cursor.fetchall()
    
    projects = [dict(row) for row in rows]
    conn.close()
    return projects


if __name__ == '__main__':
    
    unc =  str(input(" esxluir bnc: "))
    if unc == "s":
        dell_banc()
    create_db()
    
            
    