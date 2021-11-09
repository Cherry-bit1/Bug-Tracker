from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from ..Server import config
conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
    )
cursor = conn.cursor()
cursor.execute(
    """ CREATE TABLE projects (
        project_id int NOT NULL,
        project_name varchar(255) NOT NULL,
        start_date date NOT NULL,
        target_end_date date NOT NULL,
        actual_end_date date,
        created_on date NOT NULL,
        created_by varchar(255) NOT NULL,
        modified_on date NOT NULL,
        modified_by varchar(255) NOT NULL,
        PRIMARY KEY (project_id), UNIQUE KEY project_name (project_name)
    );""")

cursor.execute(
    """ CREATE TABLE people (
        person_id int NOT NULL,
        person_name varchar(255) NOT NULL,
        person_email varchar(255) NOT NULL,
        person_role varchar(30) NOT NULL,
        username varchar(255) NOT NULL,
        assigned_project int,
        created_on date NOT NULL,
        created_by varchar(255) NOT NULL,
        modified_on date NOT NULL,
        modified_by varchar(255) NOT NULL,
        PRIMARY KEY (person_id), UNIQUE KEY (person_name), UNIQUE KEY (username),
        CONSTRAINT CHK_Role CHECK (person_role = 'manager' OR person_role = 'developer' OR person_role = 'admin' OR person_role = 'submitter')
    );""")

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS issues (
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