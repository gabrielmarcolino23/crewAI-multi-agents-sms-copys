import yaml
from crewai import Agent, Task, LLM
from crewai_tools import PDFSearchTool,DOCXSearchTool
from dotenv import load_dotenv
load_dotenv()

def copywriter_lancamento_colecao():

    with open("config/agents.yaml", "r", encoding="utf-8") as file:
        agents_config = yaml.safe_load(file)

    with open("config/tasks.yaml", "r", encoding="utf-8") as file:
        tasks_config = yaml.safe_load(file)

    variaveis_tool = PDFSearchTool(pdf="./docs/variaveis.pdf")
    exemplos_tool = DOCXSearchTool(docx="./docs/exemplos.docx")

    llm = LLM(model="gpt-4o-mini-2024-07-18", temperature=0.0)  

    copywriter_lancamento_colecao_agent = Agent(
        role=agents_config["copywriter_lancamento_colecao"]["role"],
        goal=agents_config["copywriter_lancamento_colecao"]["goal"],
        backstory=agents_config["copywriter_lancamento_colecao"]["backstory"],
        verbose=agents_config["copywriter_lancamento_colecao"]["verbose"],
        tools=[variaveis_tool, exemplos_tool],
        llm=llm
    )

    copywriter_lancamento_colecao_task = Task(
        description=tasks_config["copywriter_lancamento_colecao_task"]["description"],
        expected_output=tasks_config["copywriter_lancamento_colecao_task"]["expected_output"],
        agent=copywriter_lancamento_colecao_agent,
    )

    return copywriter_lancamento_colecao_agent, copywriter_lancamento_colecao_task
