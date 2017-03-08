"""OOP showing how a typical learning institution enrolls students and hires staff """
class LearningInstitution(object):
    marks="Cut-off points"
    classes=4
    checkpoint=0
    def __init__(self, lecturers, students, supportstaff):
        self.lecturers=lectures 
        self.students=students 
        self.supportstaff=supportstaff
    def studentEnrollment(self,new):
        self.students+=new
        if(marks==True):
            print ("Allow admission")
            return self.students
        else:
            return "Deny admission"
    def lecturerHiring(self, hire):
        self.lecturers+=hire
        ratio=self.lecturers/self.students
        if(ratio<checkpoint):
           return "Hire lecturer"
        else:
            return"Hiring lecturer not advised"
    
    def newSupportStaff(self, number):
        return "Hire as seen fit"
    def head_of_institution(self):
        pass
    
class PrimarySchool(LearningInstitution):
    checkpoint=5
    def head_of_institution(self):
        return "Headteacher"
    def totalSupportstaff(self, staff=5):
        self.supportstaff+=staff
        if self.supportstaff>5:
            return "consider Budget allocation"
        else:
            return self.support
         
class secondarySchool(LearningInstitution):
    checkpoint=4
    def head_of_institution(self):
        return "Principal"

    
class university(LearningInstitution):
    checkpoint=10
    def head_of_institution(self):
        return "Chancellor"
