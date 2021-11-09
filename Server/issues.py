import datetime

class Issues(object):
    STATUS = ['OPEN', 'CLOSED']

    def __init__(self, summary, description, person1, curr_date, project, tar_date):
        self.issue_id = self.new_issue_id()
        self.issue_summary = summary
        self.issue_description = description
        self.identified_by_id = person1.person_id
        self.identified_date = curr_date
        self.related_project_id = project.project_id()
        self.assigned_to_person_id = []
        self.status = self.STATUS[0]
        self.priority = ""
        self.target_res_date = tar_date
        self.progress = ""
        self.actual_res_date = datetime()
        self.created_on = curr_date
        self.created_by = person1.person_id
        self.modified_on = datetime()
        self.modified_by = []
    

