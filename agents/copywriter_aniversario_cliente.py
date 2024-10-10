import yaml
from crewai import Agent, Task, LLM
from crewai_tools import PDFSearchTool,DOCXSearchTool
from dotenv import load_dotenv
load_dotenv()

def copywriter_aniversario_cliente():

    with open("config/agents.yaml", "r", encoding="utf-8") as file:
        agents_config = yaml.safe_load(file)

    with open("config/tasks.yaml", "r", encoding="utf-8") as file:
        tasks_config = yaml.safe_load(file)

    variaveis_tool = PDFSearchTool(pdf="./docs/variaveis.pdf")
    exemplos_tool = DOCXSearchTool(docx="./docs/exemplos.docx")

    llm = LLM(model="gpt-4o-mini-2024-07-18", temperature=0.0)  

    copywriter_aniversario_cliente_agent = Agent(
        role=agents_config["copywriter_aniversario_cliente"]["role"],
        goal=agents_config["copywriter_aniversario_cliente"]["goal"],
        backstory=agents_config["copywriter_aniversario_cliente"]["backstory"],
        verbose=agents_config["copywriter_aniversario_cliente"]["verbose"],
        tools=[variaveis_tool, exemplos_tool],
    )

    copywriter_aniversario_cliente_task = Task(
        description=tasks_config['copywriter_aniversario_cliente_task']['description'],
        expected_output=tasks_config['copywriter_aniversario_cliente_task']['expected_output'],
        agent= copywriter_aniversario_cliente_agent
    )

    return copywriter_aniversario_cliente_agent, copywriter_aniversario_cliente_task
