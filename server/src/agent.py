from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool

#Project modules
from llm import llm, memory
from tools.vector import kg_qa
from tools.cypher import cypher_qa
from tools.llmchain import chat_chain

SYSTEM_MESSAGE = """
You are a program advisor at MOSAIC, a prominent non-profit organization dedicated to supporting immigrants, refugees, 
and individuals from diverse backgrounds in Greater Vancouver and throughout British Columbia. MOSAIC offers a variety of 
programs aimed at assisting newcomers in their settlement journey.

Your task is to recommend suitable programs to users based on the information they provide about their backgrounds, needs, 
and preferences. Utilize MOSAIC's range of services to offer tailored recommendations that address the specific challenges 
and goals of each user, ultimately helping them integrate successfully into their new community.

Do not answer any questions using your pre-trained knowledge, only use the information provided in the context.
"""

tools = [
        Tool.from_function(
            name = "Vector Search Index",
            description = "Provides information about programs based on programs using Vector Search, The question will be a string. Return a string.",
            func = kg_qa
        ),
        Tool.from_function(
            name = "Graph Cypher QA Chain",
            description = "Provides information about programs including program description, age, location, services. ",
            func = cypher_qa,
            retun_direct = True
        ),
        Tool.from_function(
            name = "ChatOpenAI",
            description = "For when you need to talk about chat history. The question will be a string.  Return a string.",
            func = chat_chain.run,
            return_direct = True
        )
]

# Creationg of agent
agent = initialize_agent(
    tools,
    llm,
    memory = memory,                    
    verbose = True,
    agent =  AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    agent_kwargs = {"system_message": SYSTEM_MESSAGE}
)

def generate_response(prompt):        
    """
    Handler that calls the Conversation agent and returns  response to the Terminal.
    """
    response = agent(prompt)

    return response['output']
