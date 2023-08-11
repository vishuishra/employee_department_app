from ariadne import make_executable_schema, load_schema_from_path,snake_case_fallback_resolvers,ObjectType
from app.schema.resolvers import resolve_employee, resolve_department

query = ObjectType("Query")
query.set_field("listEmployees",resolve_department)
query.set_field("employeeInfo",resolve_employee)
type_defs = load_schema_from_path("app/graphql/schema.graphql")


schema = make_executable_schema(type_defs,query,snake_case_fallback_resolvers)