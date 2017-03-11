skills=[]
skillsStudied=[]
skillsNotStudied=[]

def add_skills():
    n=str(input("Enter skills separated by a comma: "))
    skills.append(n)
    print("skills successfully entered")

def view_skills_added():
    return skills

def indicate_skills_studied():
    i=str(input("Enter skills separated by a comma: "))
    if i not in skills:
        skills.append(i)
        skillsStudied.append(i)
    print("skills successfully indicated")

def view_skills_studied():
    return skillsStudied
    
def skills_not_studied():
    skillsNotStudied=skills-skillsStudied
    return skillsNotStudied
    

def learning_progress():
    print("skills:", skills, "skills studied: ",skillsStudied, "skills not studied: ", skillsNotStudied)

    

def skills_acquired():
    
    print("Welcome to Your skills Tracking Progress")
    print("1. Add skills\n 2.View Skills added\n 3.Skills Studied\n4.View Skills Studied\n 5.View Skills not studied\n 6.See Learning Progress ")
    option=int(input("Enter appropriate number to continue: "))
    
    
    if option==1:
        add_skills()
        
    elif option==2:
        view_skills_added()

    elif option==3:
        indicate_skills_studied()
    elif option == 4:
        view_skills_studied()
    elif option == 5:
        skills_not_studied()
    elif option == 6:
        learning_progress()
    else:
        print("Choose invalid number")


        
    

