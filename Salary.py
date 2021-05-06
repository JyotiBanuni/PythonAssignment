import os
import pandas as pd
def readEmployeeDetails(fileName):
    data = pd.read_csv(fileName, sep="\t")
    df = pd.DataFrame(data)
    fmt = '%H:%M'
    hourly_wages = 100
    df['new_end_time'] = pd.to_datetime(df['DailyEndTime'], format=fmt, errors='coerce').dt.hour
    df['new_start_time'] = pd.to_datetime(df['DailyStartTime'], format=fmt, errors='coerce').dt.hour
    df['Salary'] = (df['new_end_time']-df['new_start_time'])*hourly_wages
    del df["new_end_time"]
    del df["new_start_time"]
    return df

def getEmployeeSalary(data,EmployeeId):
    sumOfSalaries = data.groupby(by=['EmployeeId'], as_index=False)['Salary'].sum()
    empSalary = sumOfSalaries.loc[data['EmployeeId'] == EmployeeId]
    return empSalary.iloc[0]['Salary']

EmployeeId = int(input('Enter EmployeeId to get monthly salary : '))
TotalSalary = getEmployeeSalary(readEmployeeDetails("C:\\Users\dell\\Documents\\EmployeesDetails.tsv") ,EmployeeId)
file = open("C:\\Users\\dell\\Documents\\Salary.txt", "a")
file.write(" Monthly Salary  = " + str(TotalSalary)+" & EmployeeId = " + EmployeeId + os.linesep)
print("Salary is inserted in the Salary file !!")

