class TicketHashMap:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)] #crear el arreglo de 10 espacios 
        self.size = 0 # contador de tickets

    #recibe un id y regresa un indice de donde se guardó
    def _hash(self, ticket_id):
        index = ticket_id % 10
        return index

    def insert(self, ticket):
        index = self._hash(ticket.id)
        bucket = self.table[index]

        for exist in bucket:
            if exist.id == ticket.id:
                return False
            
        bucket.append(ticket)
        self.size += 1

        if self.get_load_factor() > 0.75:
            self._resize()
        return True

    def get(self, ticket_id):
        index = self._hash(ticket_id)
        bucket = self.table[index]


        for exist in bucket:
            if exist.id == ticket_id:
                return exist
        
        return None
   
    def delete(self, ticket_id):
        index = self._hash(ticket_id)
        bucket = self.table[index]
        
        for i in range(len(bucket)):
            if bucket[i].id == ticket_id:
                del bucket[i]
                self.size  -= 1
                return True
        return False

    def get_load_factor(self):
        return self.size / self.capacity

    def _resize(self):
        factor = self.get_load_factor
        old_table = self.table

        if factor > 0.75:
            self.capacity = self.capacity * 2
        
        self.table = [[] for _ in range(self.capacity)]

        for bucked in old_table:
            for ticket in bucked:
                index = self._hash(ticket.id)
                self.table[index].append(ticket)

                
