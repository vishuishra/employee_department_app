from ariadne import make_executable_schema, load_schema_from_path,snake_case_fallback_resolvers
from app.schema.resolvers import query, department_type


type_defs = load_schema_from_path("app/graphql/schema.graphql")

schema = make_executable_schema(type_defs, [query,department_type],snake_case_fallback_resolvers)



# query = ObjectType("Query")
# query.set_field("listEmployees",resolve_department)
# query.set_field("employeeInfo",resolve_employee)
