from crewai import Crew, Task

from agentes.flight_agent import create_flight_agent
from agentes.hotel_agent import create_hotel_agent
from agentes.stay_planner_agent import create_stay_planner_agent
from agentes.evaluator_agent import create_evaluator_agent

# Criando agentes
flight_agent = create_flight_agent()
hotel_agent = create_hotel_agent()
stay_agent = create_stay_planner_agent()
evaluator_agent = create_evaluator_agent()

# Criando tarefas
flight_task = Task(
    agent=flight_agent,
    description="Buscar e pontuar voos conforme regras definidas.",
    expected_output="JSON com 3 melhores opções de voo."
)

hotel_task = Task(
    agent=hotel_agent,
    description="Buscar e pontuar hotéis conforme regras definidas.",
    expected_output="JSON com 3 melhores opções de hotel."
)

stay_task = Task(
    agent=stay_agent,
    description="Decidir entre 2 ou 3 noites com base nos dados recebidos.",
    expected_output="JSON com recomendação de estadia."
)

evaluation_task = Task(
    agent=evaluator_agent,
    description="Integrar voos, hotéis e estadia e escolher o melhor plano final.",
    expected_output="JSON com o plano final da viagem."
)

# Criando a Crew
crew = Crew(
    agents=[
        flight_agent,
        hotel_agent,
        stay_agent,
        evaluator_agent
    ],
    tasks=[
        flight_task,
        hotel_task,
        stay_task,
        evaluation_task
    ],
    verbose=True
)

# Executando
if __name__ == "__main__":
    resultado = crew.kickoff()
    print("\n===== PLANO FINAL DA VIAGEM =====\n")
    print(resultado)