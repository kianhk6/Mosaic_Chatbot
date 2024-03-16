from langchain_community.graphs import Neo4jGraph
import os
from dotenv import load_dotenv

#Load variables usinig dotenv
load_dotenv()

graph = Neo4jGraph(
    url = os.getenv("NEO4J_URI"),
    username = os.getenv("NEO4J_USERNAME"),
    password = os.getenv("NEO4J_PASSWORD"),
)
