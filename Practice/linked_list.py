# this is basic node class just like struct in c
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
        
    def append(self,data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        cur = self.head
        lst = []
        while cur.next != None:
            cur = cur.next
            lst.append(cur.data)
        print(lst)

    def insert(self,index,data):
        if index > self.length():
            print('Index Out OF range')
            exit()
        new_node = node(data)
        cur = self.head
        cur_index = 0
        while cur_index != index:
            prv  = cur
            cur = cur.next
            cur_index += 1
        new_node.next = prv.next
        prv.next = new_node

    def delete(self,index):
        if self.length()<=0:
            print('Underflow')
            exit()
        cur = self.head
        cur_index = 0
        while cur_index != index:
            prv = cur
            cur = cur.next
            cur_index += 1
        prv.next = cur.next



my_list = linked_list()
my_list.display()
my_list.append(4)
my_list.display()
my_list.append(5)
my_list.append(5)
my_list.display()
my_list.insert(3,7)
my_list.display()
my_list.delete(2)
my_list.display()
