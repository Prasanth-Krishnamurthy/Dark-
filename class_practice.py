class school:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.SSLC_Mark = int(input("Enter your 10th Mark: "))

    def group(self):
        if self.SSLC_Mark > 400:
            print("You are going to Group1")
            self.stream = "Group1"
        elif self.SSLC_Mark > 300:
            print("You are going to Group2")
            self.stream = "Group2"
        elif self.SSLC_Mark >= 200:
            print("You are going to Group3")
            self.stream = "Group3"
        else:
            print("Marks too low for group allocation")
            self.stream = None

        if self.stream is not None:
            self.HSC_Mark = int(input("Enter your 12th Mark: "))


class college(school):
    def courses(self):
        if self.stream is None:
            print("Cannot proceed to college courses.")
            return

        if self.stream == "Group1" and self.HSC_Mark >= 500:
            print("You are eligible to become a Doctor, Engineer, or Scientist")
        elif self.stream == "Group2" and self.HSC_Mark >= 500:
            print("You are eligible to become a Professor, Pharmacist, or Researcher")
        elif self.stream == "Group3" and self.HSC_Mark >= 500:
            print("You are eligible to become a CEO, Chartered Accountant, or Business Analyst")

        elif self.stream == "Group1" and self.HSC_Mark >= 400:
            print("You are eligible to become a Nurse, Lab Technician, or Physiotherapist")
        elif self.stream == "Group2" and self.HSC_Mark >= 400:
            print("You are eligible to become a Teacher, Counselor, or Trainer")
        elif self.stream == "Group3" and self.HSC_Mark >= 400:
            print("You are eligible to become an Accountant, Marketing Executive, or HR Executive")

        elif self.stream == "Group1" and self.HSC_Mark >= 300:
            print("You are eligible to become a Medical Assistant, Health Worker, or Technician")
        elif self.stream == "Group2" and self.HSC_Mark >= 300:
            print("You are eligible to become a Tutor, Office Assistant, or Clerk")
        elif self.stream == "Group3" and self.HSC_Mark >= 300:
            print("You are eligible to become a Sales Executive, Supervisor, or Entrepreneur")

        else:
            print("You are not eligible for professional courses.")



student = college()   
student.group()       
student.courses()     

input("Press Enter to exit...")  
