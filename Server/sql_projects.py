import sqlite3
from projects import Projects

conn = sqlite3.connect('projects.db')
c = conn.cursor()

c.execute(""" CREATE TABLE projects (
        project_id int NOT NULL,
        project_name varchar(255) NOT NULL,
        start_date date NOT NULL,
        target_end_date date NOT NULL,
        actual_end_date date,
        created_on date NOT NULL,
        created_by varchar(255) NOT NULL,
        modified_on date NOT NULL,
        modified_by varchar(255) NOT NULL,
        PRIMARY KEY (project_id), UNIQUE (project_name)
    );""")

def insert_proj(proj):
    with conn:
        c.execute("INSERT INTO projects VALUES (?, ? ,?, ?, ?, ?, ?, ?, ?), (proj.project_id, proj.project_name, proj.start_date, proj.target_end_date, proj.actual_end_date, proj.created_on, proj.created_by, proj.modified_on, proj.modified_by)")

def get_proj_by_name(name):
    c.execute("SELECT * FROM projects WHERE project_name = ?, (name)")
    return c.fetchall()

def update_modified_on(proj, date):
    with conn:
        c.execute("""UPDATE projects SET modified_on = ?
                    WHERE project_name = ? AND project_id = ?,
                    (date, proj.project_name, proj.project_id)""")

def remove_proj(proj):
    with conn:
        c.execute("DELETE from projects WHERE project_name = ? AND project_id = ?, (proj.project_name, proj.project_id)")

conn.commit()
conn.close()
