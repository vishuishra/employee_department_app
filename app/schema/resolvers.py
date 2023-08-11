departments = [
    {"department_id": "1", "department_name": "Engineering"},
    {"department_id": "2", "department_name": "Marketing"},
    {"department_id": "3", "department_name": "Sales"},
    {"department_id": "4", "department_name": "HR"},
    {"department_id": "5", "department_name": "Admin"}

]

employees = [
    {"employee_id": "1", "employee_name": "John Doe","department_id":"1"},
    {"employee_id": "2", "employee_name": "Jane Smith","department_id":"2"},
    {"employee_id": "3", "employee_name": "Jona Smith","department_id":"1"},
    {"employee_id": "4", "employee_name": "Jerry Watson","department_id":"3"},
    {"employee_id": "5", "employee_name": "Emma Watson","department_id":"4"},
    {"employee_id": "6", "employee_name": "Sherry Boots","department_id":"2"},
    {"employee_id": "7", "employee_name": "xyz abc","department_id":"2"}
]

def resolve_employee(_, info, employeeId):
    # return next((e for e in employees if e["id"] == id), None)
    employee = next((employee for employee in employees if employee["employee_id"] == employeeId),None)
    if employee:
        employee['department'] =  next(department for department in departments if employee['department_id'] == department['department_id'])   
    return employee
    

def resolve_department(_, info, departmentId):
    department = next((department for department in departments if department["department_id"] == departmentId), None)
    if department:
        department["employees"] = [employee for employee in employees if employee["department_id"] == departmentId]
    return department


