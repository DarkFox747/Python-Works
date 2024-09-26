#Libraries
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import sys

#starndar input

lst = sys.stdin.readline().strip().split(',')
time= sys.stdin.readline().strip().split(',')
income= sys.stdin.readline().strip().split(',')
age= sys.stdin.readline().strip().split(',')
gender= sys.stdin.readline().strip()
time = [int(i) for i in time]

#Fix the inputs for sql
timeq = list([*range(time[0],time[1]+1)])
lsthexq = ','.join("'{0}'".format(x) for x in lst)
incomeq = ','.join("'{0}'".format(x) for x in income)
ageq = ','.join("'{0}'".format(x) for x in age)
timeq = ','.join("'{0}'".format(x) for x in timeq)
if gender == 'gender_female' or gender== 'gender_male':
    genderq = f"'{gender}'"
    segmentq = incomeq+","+ageq+","+genderq
else:
    genderq= "'gender_female','gender_male'"
    segmentq = incomeq+","+ageq+","+genderq

#SQL connection
database_connect = 'mysql://root:root@localhost:3306/hexlist'
engine = create_engine(database_connect)
con = engine.connect()
query = f'SELECT geography,day_part,occupancy,segment,occupancy_segment FROM hexlist.datahex WHERE geography in ({lsthexq}) AND segment in ({segmentq}) AND day_part in ({timeq})'
dataset = pd.read_sql_query(query,con)


#dataframe to complete the dataset time in case of missing rows in day_part.
df = pd.DataFrame({'day_part':[*range(0,24)]})

#Function to filter the slq data set by specific hex
def dataMod(hex):
    dataset_modified = dataset[dataset['geography']==hex]
    return dataset_modified

#Function to edit the dataset by income.
def incomeEditing(dataset_modified):
    #array of total people in  the hex // create an array of time elements = 0 
    totalPeople= np.array([*range(time[0],time[1]+1)])*0
    for j in income:
        datasetIncome = dataset_modified[dataset_modified['segment']==j]
        #Verification if the dataset is complete
        if len(datasetIncome['day_part'])<24:
            datasetIncome = pd.merge(datasetIncome,df,on='day_part', how='outer')
            datasetIncome = datasetIncome.fillna(0)
            datasetIncome = datasetIncome.sort_values('day_part')
        datasetIncome = datasetIncome.set_index('day_part')
        datasetIncome = datasetIncome.loc[int(time[0]):int(time[1]),['occupancy_segment']]
        totalPeople = np.add(totalPeople,datasetIncome['occupancy_segment'])
    return totalPeople

#Function to calculate the infomration by gender
def genderEditing(dataset_modified):
    datasetGender= dataset_modified[dataset_modified['segment']==gender]
    #Verification if the dataset is complete
    if len(datasetGender['day_part'])<24:
        datasetGender = pd.merge(datasetGender,df,on='day_part', how='outer')
        datasetGender = datasetGender.fillna(0)
        datasetGender = datasetGender.sort_values('day_part')
    datasetGender = datasetGender.set_index('day_part')
    datasetGender = datasetGender.loc[int(time[0]):int(time[1]),['occupancy','occupancy_segment']]
    datasetGender['occupancy'] = datasetGender['occupancy'].replace([0],1)
    percentageGender = np.divide(datasetGender['occupancy_segment'],datasetGender['occupancy'])
    return percentageGender

#Function to calculate the information by age
def ageEditing(dataset_modified):
    totalPeople= np.array([*range(time[0],time[1]+1)])*0
    for i in age:
        datasetAge = dataset_modified[dataset_modified['segment']==i]
        #Verification if the dataset is complete
        if len(datasetAge['day_part'])<24:
            datasetAge = pd.merge(datasetAge,df,on='day_part', how='outer')
            datasetAge = datasetAge.fillna(0)
            datasetAge = datasetAge.sort_values('day_part')
        datasetAge = datasetAge.set_index('day_part')
        datasetAge = datasetAge.loc[int(time[0]):int(time[1]),['occupancy','occupancy_segment']]
        datasetAge['occupancy'] = datasetAge['occupancy'].replace([0],1)
        percentageAge = np.divide(datasetAge['occupancy_segment'],datasetAge['occupancy'])
        totalPeople = np.add(totalPeople,percentageAge)
    return totalPeople

#Function to execute the script and return the hex with the occupancy
def calculate():    
    for i in lst:
        dataMin = dataMod(i)
        minPeople = incomeEditing(dataMin)
        multAge = ageEditing(dataMin)
        if gender !=  'all':            
            multGender = genderEditing(dataMin)            
            total = minPeople * multGender * multAge
            total = np.sum(total)
            print(i,total)
        else:
            total = minPeople * multAge
            total = np.sum(total)
            print(f"{i},{total}")    
    
#Make the script work
def main():
    calculate()

if __name__ == "__main__":
    main()
