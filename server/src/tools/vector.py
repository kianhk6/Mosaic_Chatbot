from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.chains import RetrievalQA

import os
from dotenv import load_dotenv

#project modules
from llm import llm, embeddings

#Load variables usinig dotenv
load_dotenv()

#Neo4j vector storage for the embeddings
neo4j_vector = Neo4jVector.from_existing_index(
    embeddings,
    url = os.getenv("NEO4J_URI"),
    username = os.getenv("NEO4J_USERNAME"),
    password = os.getenv("NEO4J_PASSWORD"),
    index_name = "programDescription",
    node_label = "Program",
    text_node_property = "description",
    embedding_node_property = "embedding",
    retrieval_query = """
    RETURN
        node.description AS text,
        score,
        {   
            service : [ (node)-[:PROVIDES]->(s:Service) | s.name ],
            age : [ (node)-[:AVAILABLE_FOR]->(ag:Age) | ag.name ],
            location :  [ (node)-[:AVAILABLE_IN]->(loc:Location) | loc.name ],
            status : [ (node)-[:STATUS]->(st:Status) | st.name ]
        } AS metadata
        """
)

# Returns the vector storage as a retriever
retriever = neo4j_vector.as_retriever()

#Chain to user the retriever to pass documents to the LLM
#"stuff" inserts documents into the prompt
kg_qa = RetrievalQA.from_chain_type(
    llm,
    chain_type="stuff",
    retriever=retriever,
    verbose = True,
    return_source_documents=True
)
