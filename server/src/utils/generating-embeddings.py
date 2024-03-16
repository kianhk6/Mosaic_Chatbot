import os 
import openai
from neo4j import GraphDatabase, Result
import pandas as pd
from openai import OpenAI, APIError
from dotenv import load_dotenv
from time import sleep


load_dotenv()

class ProgramVectorSearchIndexConfiguration:
    """
    Class used to create the embeddings from program descriptions
    Used to create an index in Neo4j before using the chatbot
    """

    def __init__(self):
        """
        Connect to the database
        """
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
        )
        self.driver.verify_connectivity()

    def collect_programs(self, limit=None):

        """Collect all programs that have a program description"""
        query = """ MATCH (p:Program)
                     WHERE p.description IS NOT NULL
                     RETURN ID(p) AS program_id, p.name AS program_name, p.description AS program_description"""
        
        if limit is not None:
            query += f" LIMIT {limit}"

        programs = self.driver.execute_query(
            query,
            result_transformer_ = Result.to_df
        )

        print(len(programs))

        return programs
    
    def generate_embeddings(self, file_name: str, programs: pd.DataFrame):
        """Create embeddings for program descriptions using OpenAI text-to-embedding-ada-002"""
        openai_api_key = os.getenv("OPENAI_API_KEY")
        client = OpenAI()

        embeddings = []
        for _, n in programs.iterrows():

            successful_call = False 
            while not successful_call:
                try:
                    res = client.embeddings.create(
                        model = "text-embedding-ada-002",
                        input = f"{n['program_name']}: {n['program_description']}",
                        encoding_format = "float")
                    successful_call = True
                except APIError as e:
                    print(e)
                    print("Retrying in 5 seconds")
                    sleep(5)
            print(n['program_name'])

            embeddings.append({
                "program_id": n['program_id'],
                "embedding": res.data[0].embedding
            })

        embeddings_df = pd.DataFrame(embeddings)
        embeddings_df.head()
        embeddings_df.to_csv(file_name, index=False)

    def close(self):
        """Close the database connection"""
        self.driver.close()
    
config = ProgramVectorSearchIndexConfiguration()
config.generate_embeddings("program_embeddings.csv", config.collect_programs())
config.close()
print("Embeddings created!")