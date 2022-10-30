#importing the modules
import pandas as pd # Type 'pip install pandas' to install pandas in your system
import random as r 
#For getting input from the excel sheet
Input = pd.read_csv(r"C:\Users\bhara\OneDrive\Desktop\ZPHS GROUPS\Data.csv")
#To store the list of Name,Roll_Num,Gmail
list1 = list(Input['Name']) 
list2 = list(Input['Roll_Num'])
list3 = list(Input['Gmail']) 
#To store the inputs into another Empty list
Name=[]
Roll_Num=[]
Gmail=[]
#to Generate random numbers
s=list(range(0,25))
d=r.sample(s,k=25)
#Loop To divide the values into group
j=0
gn=[] #group number
z=1
for i in range(0,5):
    count=5
    while(count!=0):
        a=d[j]
        j=j+1
        gn.append(z)
        Name.append(list1[a])
        Roll_Num.append(list2[a])
        Gmail.append(list3[a])
        count=count-1   
    z=z+1
#To create dictonary
Group1={'Group':gn,'Name':Name,'Roll-Num':Roll_Num,'Gmail':Gmail}
#To create data frame
GroupData=pd.DataFrame.from_dict(Group1)
#To store the output in Excel
GroupData.to_csv(r'C:\Users\bhara\OneDrive\Desktop\ZPHS GROUPS\Output\team1.csv',index=False)
print(GroupData)
    





