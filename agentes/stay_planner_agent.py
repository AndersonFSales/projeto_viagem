from crewai import Agent

def create_stay_planner_agent():
    with open("prompts/stay_prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()

    return Agent(
        role="Stay Planner Agent",
        goal="Decidir entre 2 ou 3 noites com base em custo e logística.",
        backstory="Planejador de estadia focado em descanso pré-prova.",
        verbose=True,
        allow_delegation=False,
        memory=False,
        prompt=prompt
    )