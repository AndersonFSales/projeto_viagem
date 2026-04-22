from crewai import Agent

def create_evaluator_agent():
    with open("prompts/evaluator_prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()

    return Agent(
        role="Evaluator Agent",
        goal="Integrar voos, hotéis e estadia para escolher o melhor plano.",
        backstory="Analista especializado em decisões multi-critério.",
        verbose=True,
        allow_delegation=False,
        memory=False,
        prompt=prompt
    )