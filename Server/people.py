class People(object):
    ROLES = ['manager', 'developer', 'admin', 'submitter']

    def __init__(self):
        self.person_id = 0
        self.person_name = ""
        self.email = ""
        self.role = ""
        self.username = ""
        self.assigned_project = []