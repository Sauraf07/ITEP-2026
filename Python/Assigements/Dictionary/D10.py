employees = {
    "emp1": {"salary": 5000},
    "emp2": {"salary": 7000}
}
emp1 = {employees["emp1"]["salary"]}
emp2 = {employees["emp2"]["salary"]}
print(f"Salary of employee1 : {emp1}")
print(f"Salary of employee1 : {emp2}")
print(f"total  : {employees['emp1']["salary"] + employees['emp2']["salary"]} ")