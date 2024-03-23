class Node:
    # Create the node of the linked list
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    # Create the empty list
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, data, index=None):
        # if index is none then insert at start
        if index is None:
            node = Node(data, self.head)
            self.head = node
        # if index is less than 0 then insert at last
        if index < 0:
            itr = self.head
            while itr.next:
                itr = itr.next
            node = Node(data, None)
            itr.next = node
        if index >= 0 and index < self.getLength():
            count = 0
            itr = self.head
            while itr:
                if count-1 == index:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print(self):
        itr = self.head
        data = ""
        while itr:
            data += itr.data + "-->"
            itr = itr.next
        print(data[0:len(data)-3])

if __name__=="__main__":
    ll = LinkedList()
    ll.getLength()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.print()

    
