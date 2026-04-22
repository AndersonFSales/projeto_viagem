from crewai import Agent

def create_hotel_agent():
    with open("prompts/hotel_prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()

    return Agent(
        role="Hotel Agent",
        goal="Encontrar hotéis ideais com café da manhã e boa localização.",
        backstory="Especialista em hospedagem para atletas.",
        verbose=True,
        allow_delegation=False,
        memory=False,
        prompt=prompt
    )