from crewai import Agent

def create_flight_agent():
    with open("prompts/flight_prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()

    return Agent(
        role="Flight Agent",
        goal="Encontrar e pontuar as melhores opções de voo.",
        backstory="Especialista em logística aérea para atletas.",
        verbose=True,
        allow_delegation=False,
        memory=False,
        prompt=prompt
    )