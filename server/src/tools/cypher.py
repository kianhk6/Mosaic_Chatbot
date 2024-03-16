from langchain.chains import GraphCypherQAChain
from langchain.prompts.prompt import PromptTemplate
    
from llm import llm
from graph import graph

CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cpyher to answer questions about programs
Convert the user's question based on the schema .

Instructions:
Use only the provided relationships types and properties in the schema.
Do not use any other relationships typpes or properties that are not provided.

Example Cypher Statement:
1. What services are available?
```
MATCH (p:Program)-[:PROVIDES]->(s:Service)
```

Schema:
{schema}

Question:
{question}
"""

cypher_prompt = PromptTemplate.from_template(CYPHER_GENERATION_TEMPLATE)

#Graph enabled semantic search to use the neo4j graph database
cypher_qa = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    # verbose=True,
    cypher_prompt=cypher_prompt,
)
