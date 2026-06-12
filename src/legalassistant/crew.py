from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from crewai.agents.agent_builder.base_agent import BaseAgent

from legalassistant.tools.ipc_sections_search_tool import (
    search_ipc_sections
)

from legalassistant.tools.legal_precedent_search_tool import (
    search_legal_precedents
)

@CrewBase
class LegalAssistant:
    """Legal Assistant Crew"""
    
    # agents= list[BaseAgent]
    # tasks= list[Task]
    
    agents_config= "config/agents.yaml"
    tasks_config= "config/tasks.yaml"
    
    ####################### AGENT DEFINITIONS #######################
    @agent
    def case_intake_agent(self)->Agent:
        return Agent(
            config=self.agents_config["case_intake_agent"],
            verbose=True
        )   
    
    @agent
    def ipc_section_agent(self)->Agent:
        return Agent(
            config=self.agents_config["ipc_section_agent"],
            tools=[search_ipc_sections],
            verbose=True
        )
    
    @agent
    def legal_precedent_agent(self)->Agent:
        return Agent(
            config=self.agents_config["legal_precedent_agent"],
            tools=[search_legal_precedents],
            verbose=True
        )
    
    @agent
    def legal_drafter_agent(self)->Agent:
        return Agent(
            config=self.agents_config["legal_drafter_agent"],
            verbose=True
        )
        
    ####################### TASK DEFINITIONS #######################
    
    @task
    def case_intake_task(self)->Task:
        return Task(
            config=self.tasks_config["case_intake_task"]
        )
    
    @task
    def ipc_section_task(self)->Task:
        return Task(
            config=self.tasks_config["ipc_section_task"]
        )
    
    @task
    def legal_precedent_task(self)->Task:
        return Task(
            config=self.tasks_config["legal_precedent_task"]
        )
    
    @task
    def legal_drafter_task(self)->Task:
        return Task(
            config=self.tasks_config["legal_drafter_task"]
        )
    
    ##################### Crew Definition #####################
    @crew
    def crew(self)->Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
    