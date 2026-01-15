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

    # 1️⃣ Cria a tabela (caso não exista)
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {NAME_TABLE}(
            project_id TEXT PRIMARY KEY,
            categoria TEXT,
            publicado TEXT,
            nivel TEXT,
            titulo TEXT,
            descriçao TEXT,
            link TEXT
        )
    ''')

    # 2️⃣ Verifica se a coluna data_criacao existe
    cursor.execute(f"PRAGMA table_info({NAME_TABLE})")
    colunas = [col[1] for col in cursor.fetchall()]

    # 3️⃣ Se não existir, adiciona
    if 'data_criacao' not in colunas:
        cursor.execute(f'''
            ALTER TABLE {NAME_TABLE}
            ADD COLUMN data_criacao DATETIME
        ''')

        # (opcional) Preenche registros antigos
        cursor.execute(f'''
            UPDATE {NAME_TABLE}
            SET data_criacao = DATETIME('now','localtime')
            WHERE data_criacao IS NULL
        ''')

        print("🗓️ Coluna data_criacao adicionada com sucesso!")

    conn.commit()
    conn.close()
    
    

def save_to_db(list_projects,):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for project in list_projects:
        
        cursor.execute(f'''
            INSERT OR IGNORE INTO {NAME_TABLE}
            (project_id, categoria, publicado, nivel, titulo, descriçao, link, data_criacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, DATETIME('now','localtime'))
            ''', (
            project['ID'],
            project['categoria'],
            project['publicado'],
            project['nivel'],
            project['titulo'],
            project['descriçao'],
            project['link']
        ))

    
    conn.commit()
    conn.close()
    print(f"Processo finalizado: novos projetos processados.")


def read_data():
    
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(f'''
        SELECT *
        FROM {NAME_TABLE}
        WHERE DATE(data_criacao) = DATE('now','localtime')
    ''')

    rows = cursor.fetchall()
    projects = [dict(row) for row in rows]

    conn.close()
    return projects


if __name__ == '__main__':
    
    unc =  str(input(" esxluir bnc: "))
    if unc == "s":
        dell_banc()
    create_db()
    
            
    