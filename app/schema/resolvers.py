from ariadne import ObjectType,QueryType

query = QueryType() #QueryType defines the root-level queries that clients can request to retrieve data. 
                    #It's the starting point for data fetching.

department_type = ObjectType("Department") #ObjectType defines custom types that can represent various structured data, including objects, relationships, and other types of data. 
                                            #They are not just for queries but can be used for defining the shape of data throughout your schema
# employee_type = ObjectType("Employee")

# dummy data
departments_data = [
    {"department_id": "1", "department_name": "Engineering"},
    {"department_id": "2", "department_name": "Marketing"},
    {"department_id": "3", "department_name": "Sales"},
    {"department_id": "4", "department_name": "HR"},
    {"department_id": "5", "department_name": "Admin"}

]

employees_data = [
    {"employee_id": "1", "employee_name": "John Doe","department_id":"1"},
    {"employee_id": "2", "employee_name": "Jane Smith","department_id":"2"},
    {"employee_id": "3", "employee_name": "Jona Smith","department_id":"1"},
    {"employee_id": "4", "employee_name": "Jerry Watson","department_id":"3"},
    {"employee_id": "5", "employee_name": "Emma Watson","department_id":"4"},
    {"employee_id": "6", "employee_name": "Sherry Boots","department_id":"2"},
    {"employee_id": "7", "employee_name": "xyz abc","department_id":"2"}
]




@query.field("departments")
def resolve_departments(_,info):
    return departments_data


@query.field("employeeByDepartmentId")
def resolve_employee_by_department_id(_, info,departmentId):
    for department in departments_data:
        if department['department_id'] == departmentId:
            return department


@department_type.field("employees")
def resolve_department_employees(department_type, info):
    """
    departmennt_type: This argument represents the parent object (Author) that the field resolver is resolving for. 
    In other words, it's the instance of the department type that's being resolved.
    You can access its properties and use them to determine the result of the resolver. 
    """   
    return [employee for employee in employees_data if employee['department_id'] == department_type['department_id']]









# def resolve_employee(_, info, employeeId):
#     # return next((e for e in employees if e["id"] == id), None)
#     employee = next((employee for employee in employees if employee["employee_id"] == employeeId),None)
#     if employee:
#         employee['department'] =  next(department for department in departments if employee['department_id'] == department['department_id'])   
#     return employee
    

# def resolve_department(_, info, departmentId):
#     department = next((department for department in departments if department["department_id"] == departmentId), None)
#     if department:
#         department["employees"] = [employee for employee in employees if employee["department_id"] == departmentId]
#     return department


