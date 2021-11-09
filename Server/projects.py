import datetime
class Projects(object):

    def __init__(self, people, name, end_date):
        self.project_id = 0
        self.project_name = name
        self.start_date = datetime()
        self.target_end_date = end_date
        self.actual_end_date = datetime()
        self.created_on = datetime.datetime.now()
        self.created_by = people.person_id
        self.modified_on = datetime()
        self.last_modified_by = people.person_id


