class User:
    def __init__(self, id=0, email="", password_hash="", first_name="", last_name="",
                 org_number=0, department=None, company=None, role=""):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.org_number = org_number
        self.department = department
        self.company = company
        self.role = role