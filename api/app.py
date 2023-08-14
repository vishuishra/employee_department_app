from fastapi import FastAPI
from ariadne.asgi import GraphQL
from app.schema.types import schema


app = FastAPI()

graphQL = GraphQL(schema, debug=False)


app.mount("/", graphQL)










# app = GraphQL(schema, debug=True)


#  type_defs = load_schema_from_path("graphql/schema.graphql")
# resolvers = [query, mutation, subscription]
# schema = make_executable_schema(type_defs, resolvers, snake_case_fallback_resolvers)

# from ariadne import QueryType, make_executable_schema, load_schema_from_path
# from ariadne.asgi import GraphQL

# type_defs = load_schema_from_path("schema.graphql")

# query = QueryType()


# @query.field("hello")
# def resolve_hello(*_):
#     return "Hello world!"


# schema = make_executable_schema(type_defs, query)
# app = GraphQL(schema, debug=True)
