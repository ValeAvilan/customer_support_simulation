from data_structures.ticket_hashmap import TicketHashMap
from data_structures.ticket_queue import TicketQueue


class SupportSystem:
    def __init__(self):
        self.tickets = TicketHashMap()
        self.pending_queue = TicketQueue()

    def add_ticket(self, ticket): 
        insert = self.tickets.insert(ticket) #devuelve true o false
        if insert: #si fue true se agrega a queue
            self.pending_queue.enqueue(ticket.id) 
        return insert

    def process_next_ticket(self): #cambiar estados del ticket
        ticket_id = self.pending_queue.dequeue()
        if ticket_id is None:
            return None
        
        ticket = self.tickets.get(ticket_id)
        if ticket is None:
            return None
        
        ticket.status = 'In Progress'
        return ticket
    
    def assign_ticket(self, ticket_id, agent):
    # 1. Buscar el ticket en el Hash Map
        ticket = self.tickets.get(ticket_id)

    # 2. Si no existe, devolver False
        if ticket is None:
            return None

    # 3. Comprobar que el ticket esté "In Progress"
    # 4. Comprobar que no tenga ya un agente asignado
    # 5. Guardar el agente en ticket.assigned_agent
    # 6. Agregar ticket_id a agent.active_tickets
    # 7. Devolver True
        if ticket.status == 'In Progress':
            if ticket.assigned_agent is None:
                ticket.assigned_agent = agent
                agent.active_tickets.append(ticket_id)
                return True
        return False
                
                


   



    