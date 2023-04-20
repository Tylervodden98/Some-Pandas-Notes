import pandas as pd
import datetime

# Series exercise
dict_emp = {
    "ID": 1,
    "Name": "Tyler",
    "Salary": 40000,
    "Department": "Finance",
    "Start Date": datetime.datetime.now(),
    "Currently Employed": True
}

dict_emp2 = {
    "ID": 2,
    "Name": "Bob",
    "Salary": 60000,
    "Department": "Finance",
    "Start Date": datetime.datetime.now(),
    "Currently Employed": True
}

dict_emp3 = {
    "ID": 3,
    "Name": "Jill",
    "Salary": 30000,
    "Department": "HR",
    "Start Date": datetime.datetime.now(),
    "Currently Employed": True
}

first = pd.Series(data=dict_emp)
second = pd.Series(data=dict_emp2)
third = pd.Series(data=dict_emp3)

final = pd.Series([first, second, third], index=[
                  first["ID"], second["ID"], third["ID"]])
print(final)

# Dataframe Exercise
employee_df = pd.DataFrame(final)
print(employee_df)

# Dataframe from list
emp_df = pd.DataFrame([first, second, third], index=[
                      first["ID"], second["ID"], third["ID"]])
print(emp_df)

# Dataframe from dict
emp_dictdf = pd.DataFrame([dict_emp, dict_emp2, dict_emp3], index=[
                          dict_emp["ID"], dict_emp2["ID"], dict_emp3["ID"]])
print(emp_dictdf)

# Dataframe operations
# Sum column Salary
sum = emp_df['Salary'].sum()
print(sum)

# For avg
avg = emp_df['Salary'].mean()
print(f"\nAvg Salary is {avg}")

# For Min
min = emp_df["Salary"].min()
print(f"\nMin Salary is {min}")

# For Max
max = emp_df["Salary"].max()
print(f"\nMax Salary is {max}")

# Now find these measurements by department
department_df = emp_df[["Salary", "Department"]].groupby(
    'Department').agg(['sum', 'max', 'min', 'mean'])
print(department_df)

# Seperate DF of Departments and Merge onto EMP df
departments_dataf = pd.DataFrame({"Department": ["HR", "CEO", "IT", "Accounting"]})
print(departments_dataf)

#Join emp_df with Department Dataframe (Only keeps matching departments)
print(emp_df.merge(departments_dataf))

#Give everyone a 10% raise
emp_df["Salary"] = emp_df["Salary"] * 1.1
print("Gave everyone 10% raise!")
print(emp_df)
