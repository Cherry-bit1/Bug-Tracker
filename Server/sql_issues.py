import sqlite3
from issues import Issues

conn = sqlite3.connect('issues.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS issues (
        issue_id int NOT NULL,
        issue_summary varchar(255) NOT NULL,
        issue_description varchar(4000),
        identified_by_person_id int NOT NULL,
        identified_date date NOT NULL,
        related_project int NOT NULL,
        assigned_to int,
        status varchar(30) NOT NULL,
        priority varchar(30),
        target_resolution_date date,
        progress varchar(4000),
        actual_resolution_date date,
        resolution_summary char(4000),
        created_on date NOT NULL,
        created_by varchar(255) NOT NULL,
        modified_on date NOT NULL,
        modified_by varchar(255) NOT NULL,
        PRIMARY KEY (issue_id),
        FOREIGN KEY (identified_by_person_id) REFERENCES people (person_id),
        FOREIGN KEY (related_project) REFERENCES project (project_id),
        FOREIGN KEY (assigned_to) REFERENCES people (person_id),
        CONSTRAINT CHK_Status CHECK (actual_resolution_date = null),
        CONSTRAINT CHK_Priority CHECK (priority <= 5)
    );""")

def insert_issue(issue):
    with conn:
        c.execute("INSERT INTO issues VALUES (?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?), (issues.issue_id, issues.issue_summary, issues.issue_description, issues.identified_by_person_id, issues.identified_date, issues.related_project, issues.assigned_to, issues.status, issues.priority, issues.target_resolution_date, issues.progress, issues.actual_resolution_date, issues.resolution_summary, issues.created_on, issues.created_by, issues.modified_on, issues.modified_by)")

def get_issue_by_id(id):
    c.execute("SELECT * FROM issues WHERE issue_id = ?, (id)")
    return c.fetchall()

def get_issue_by_related_project(project):
    c.execute("SELECT * FROM issues WHERE related_project = ?, (project.project_id)")
    return c.fetchall()

def get_issue_by_assignment(person):
    c.execute("SELECT * FROM issues WHERE assigned_to = ?, (person.person_id)")
    return c.fetchall()

def remove_issue(issue):
    with conn:
        c.execute("DELETE from issues WHERE issue_id = ?, (issue.issue_id)")

conn.commit()
conn.close()