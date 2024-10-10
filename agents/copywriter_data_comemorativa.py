import yaml
from crewai import Agent, Task, LLM
from crewai_tools import PDFSearchTool,DOCXSearchTool
from dotenv import load_dotenv
load_dotenv()

def copywriter_data_comemorativa():

    with open("config/agents.yaml", "r", encoding="utf-8") as file:
        agents_config = yaml.safe_load(file)

    with open("config/tasks.yaml", "r", encoding="utf-8") as file:
        tasks_config = yaml.safe_load(file)

    variaveis_tool = PDFSearchTool(pdf="./docs/variaveis.pdf")
    exemplos_tool = DOCXSearchTool(docx="./docs/exemplos.docx")

    llm = LLM(model="gpt-4o-mini-2024-07-18", temperature=0.0)  

    copywriter_data_comemorativa_agent = Agent(
        role=agents_config["copywriter_data_comemorativa"]["role"],
        goal=agents_config["copywriter_data_comemorativa"]["goal"],
        backstory=agents_config["copywriter_data_comemorativa"]["backstory"],
        verbose=agents_config["copywriter_data_comemorativa"]["verbose"],
        tools=[variaveis_tool, exemplos_tool],
        llm=llm
    )

    copywriter_data_comemorativa_task = Task(
        description=tasks_config['copywriter_data_comemorativa_task']['description'],
        expected_output=tasks_config['copywriter_data_comemorativa_task']['expected_output'],
        agent=copywriter_data_comemorativa_agent
    )

    return copywriter_data_comemorativa_agent, copywriter_data_comemorativa_task
