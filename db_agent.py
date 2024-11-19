from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
import pandas as pd
import os
from sqlalchemy import create_engine
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase

#instantiating model
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    groq_api_key = "..",
    temperature=0,
)

#DB creation from CSV
database_path = "./db/salary.db"
os.makedirs(os.path.dirname(database_path), exist_ok=True)
engine = create_engine(f"sqlite:///{database_path}")
df = pd.read_csv("salaries_2023.csv").fillna(value=0)
df.to_sql("salaries_data", con=engine, if_exists='replace', index=False)
print(f"DB {df} created successfully")

db = SQLDatabase.from_uri(f"sqlite:///{database_path}")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

sql_agent = create_sql_agent(toolkit=toolkit, llm=llm, verbose=True)

queston = """
    what is the highest avg salary by dept and given me the number
"""

res = sql_agent.invoke(queston)
print(res)
