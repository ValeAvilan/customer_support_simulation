class Node:
    def __init__(self, ticket_id):
        self.value = ticket_id
        self.next = None

class TicketQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, ticked_id):
        new_node = Node(ticked_id)

        if self.size == 0:
            self.head = new_node
        else:
            self.tail.next = new_node 

        self.tail = new_node
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            return None
        
        curr = self.head

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            curr.next = None
        self.size -= 1

        return curr.value

    def peek(self):
        if not self.head:
            return None
        else:
            return self.head.value

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
        

