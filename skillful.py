#prompt = "Enter the job skills for at least six jobs in which you are interested: "
#print(prompt)

job_skills = ['hive', 'spark']
prompt = "Enter a job skill: "

active = True
while active:
    new_skill = input(prompt)
    job_skills.append(new_skill)
    
    print(f"Skill Added!")

    if new_skill == 'quit':
        active = False

        job_skills.remove('quit')

import collections
collections.Counter(job_skills)

#print(job_skills)



    
         


             

"""
for job_skill in job_skills:
   
print(job_skills)            """


#print("\nSkill added!")

"""new_skill = len(job_skills)
print('This list is {} elements long'.format(job_skills))

while job_skills:
    
print(f"\nAdding New Skill: {new_skill} to list")
print(job_skills)                   """
                                       


#print("\nThe following skills have been added:")
#print(job_skills)"""




