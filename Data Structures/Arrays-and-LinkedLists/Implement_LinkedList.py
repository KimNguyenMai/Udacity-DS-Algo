class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

def CreateLinkedList(inputList):
    i = 0
    head = None
    tail = None
    
    if len(inputList == 0):
        return None
    else: 
        for val in inputList:
            if head == None:
                head = Node(val)
                tail = head
            else: 
                tail = Node(val)

    return head

inputlist = [1,2,3,4]
CreateLinkedList(inputlist)
