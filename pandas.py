#1question
#We can use any types like lists,dictionaries,arrays,typles 

#2question
import pandas as pd
data=[1,2,3,4,5,6,7,8,9,10,11,12]
index=["January","February","March","April","May","June","July","August","September","October","November","December"]
month_series=pd.Series(data,index)
print(month_series)
#3question
import pandas as pd
student_data = {
    'MatMIE': 30,  
    'Mat DAIS': 25,  
    'COMIE': 28,  
    'COMEC': 35 }
student_series = pd.Series(student_data)
print(student_series)
#4question
import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
df = pd.DataFrame(exam_data,labels)
print(df)
#5question
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
filtered_df = df[df['attempts'] > 2]

print("Number of attempts in the examination is greater than 2:")
print(filtered_df)
