class User:
    name = None
    email = None
    def _init_(self,name,email):
        self.name = name
        self.email = email
    def send_email(self):
        if self.email is not None:
            print("sending email: "+self.email)
        else:
            print("Error")
    def _str_(self):
        return "User: "+self.name+", "+self.email

class Student(User):
    def is_approved(self):
        return self.score >= 8
    score = None
    def _init_(self, name=None, email=None,score=None):
        super()._init_(name, email)
        self.score=score
    def _str_(self):
        return "Student: "+self.name+", "+self.email+"score: "+str(self.score)
    def _repr_(self):
        name = self.name
        email = self.email
        score = self.score
        return f"Student({name=},{email=},{score=})"
