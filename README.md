# Database Interaction Agent using LangChain

This repository contains a project that demonstrates how to create an AI-powered **SQL Agent** using **LangChain** to interact with a database. The agent is capable of querying a SQLite database and responding intelligently using a large language model (LLM).

---

## 📝 Features

1. **Database Creation**:  
   A SQLite database is dynamically created from a CSV file (`salaries_2023.csv`) containing salary data.
   
2. **SQL Agent**:  
   An AI agent is built using the LangChain framework and is capable of interacting with the database to execute SQL queries and return results in natural language.

3. **LLM Integration**:  
   The agent is powered by **Llama-3.1-70b-versatile** model, instantiated via `ChatGroq`. This model helps interpret user queries and generates corresponding SQL commands.

4. **Query Example**:  
   The agent can process complex natural language questions, such as:  
   - _"What is the highest average salary by department and give me the number?"_

---

## 🚀 How It Works

1. **Database Setup**:  
   - A SQLite database is created from a CSV file (`salaries_2023.csv`), and the data is saved in a table named `salaries_data`.

2. **AI Agent Setup**:  
   - The SQL Agent is initialized with the `LangChain` framework, using the `ChatGroq` LLM to process and interpret user questions.

3. **Query Execution**:  
   - The agent converts natural language queries into SQL commands and executes them on the database. The results are returned to the user in a user-friendly format.

---

**Clone the Repository**:  
   ```bash
   conda create -n venv python=3.10.15
   git clone https://github.com/ThisIsFarhan/DB-Agent.git
   cd DB-Agent
```

