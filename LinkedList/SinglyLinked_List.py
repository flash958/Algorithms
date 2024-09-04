class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    '''Insertion of Element from the last into the Singly Linklist'''
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

        self.length+=1

    '''Insertion of Element from the beginning into the Singly Linklist'''

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    ''' Inserting Element at specific index in the linked list'''

    def insert_at_index(self,value,index):
        new_node=Node(value)
        temp_node=self.head
        for i in range(index-1):
            temp_node=temp_node.next
        new_node.next=temp_node.next
        temp_node.next=new_node
        self.length+=1


    ''' Method to traverse the Singly Linklist'''

    def tranverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current=current.next

    ''' Searching the element in the Linked list'''
    def search(self, value):
        current=self.head
        index=0
        while current:
            if (current.value == value):
                print("Value found at index : ", index)
                break

            index += 1
            current=current.next

    ''' Getting the element based on the index'''
    def get(self, index):



        if(index==-1):
            return self.tail.value
        if(index<-1 and index>=self.length):

            return None


        current=self.head

        for i in range(index):
            current=current.next
        return current.value

    '''Popping the Elements in Linked list from Beginning'''
    def pop_first(self):
        popped_node=self.head
        self.head=self.head.next
        popped_node.next=None
        self.length-=1
        return popped_node

    ''' Popping the Element from the last'''
    def pop(self):
        popped_node=self.tail
        if(self.length==1):
            self.head=None
            self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            self.tail=temp
            temp.next=None
        self.length-=1
        return popped_node

    ''' Removing specific elements based on the index'''
    def remove(self,index):
        prev_node=self.get(index)
        popped_node=prev_node.next
        prev_node.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node

    ''' Deleting all ths elements from the linked list'''
    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0




















    def __str__(self):
        temp_node = self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+='->'
            temp_node=temp_node.next

        return result


new_linked_list=LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepend(40)
new_linked_list.append(30)
new_linked_list.append(50)
new_linked_list.prepend(60)
new_linked_list.insert_at_index(90,1)

print(new_linked_list.length)
print(new_linked_list)
new_linked_list.tranverse()
new_linked_list.search(60)
print(new_linked_list.get(3))
print(new_linked_list.pop_first().value)
print(new_linked_list)
print(new_linked_list.pop_first().value)
print(new_linked_list)




