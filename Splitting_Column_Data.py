import codecademylib3_seaborn
import pandas as pd
from students import students  ## Import Data

print(students.columns) 
print(students.gender_age.head()) 

students['gender'] = students.gender_age.str[0]   ## Set the values in a new column in the students DataFrame called 'gender' to the zeroth index of the data in the gender_age column
students['age'] = students.gender_age.str[1:]  ## Set the values in a new column in the students DataFrame called 'age' to the remaining indexes of the data in the gender_age column
print(students.head())
students_new = students[['full_name','exam','grade','score','gender','age']]  ## remove the gender_age column ... it's not needed anymore

print(students_new)

