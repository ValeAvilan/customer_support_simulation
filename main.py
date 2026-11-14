from models.ticket import Ticket
from models.agent import Agent
from services.support_system import SupportSystem

system = SupportSystem()
carlos = Agent(1, "Carlos")
ana = Agent(2, "Ana")

system.add_ticket(Ticket(101, "Login problem", 2, "Technical"))

print(system.assign_ticket(101, carlos))  # False: todavía está Pending

system.process_next_ticket()

print(system.assign_ticket(101, carlos))  # True
print(system.assign_ticket(101, ana))     # False: ya está asignado

ticket = system.tickets.get(101)

print(ticket.assigned_agent.name)         # Carlos
print(carlos.active_tickets)              # [101]
print(ana.active_tickets)                 # []