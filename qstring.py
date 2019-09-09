class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def enque(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.head
            self.head=newnode

    def deque(self):
        if(self.head==None):
            print("Empty List")
        else:
            temp=self.head
            while(temp.next is not None):
                prev = temp
                temp = prev.next
            self.tail=prev
            self.tail.next=None

    def searching(self,key):
        val=input()
        if(self.head==None):
            print("Empty List")
        else:
            temp=self.head
            while(temp.data is not key):
                if(temp.next is not None):
                    temp=temp.next
                else:
                    print("String is not found:(")
                    break
            else:
                print("String is found:)")
            temp=None

    def updating(self,newv):
        if(self.head==None):
            print("Empty List")
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.data=newv

    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

s=Queue()
print("**Ready to perform Queue**")
while(True):
    print("Operations")
    print("Select required operation?")
    print("<<1. Enque>>")
    print("<<2. Deque>>")
    print("<<3. Searching>>")
    print("<<4. Updation>>")
    print("<<5. Display>>")
    print("<<6. Exit>>")
    n=input()
    if(n is "1"):
        print("Enter String to be enqued")
        val=input()
        s.enque(val)
    elif(n is "2"):
        s.deque()
    elif(n is "3"):
        print("Enter string to be searched")
        
        s.searching(val)
    elif(n is "4"):
        print("Enter the new string")
        val1=input()
        s.updating(val1)
    elif(n is "5"):
        s.display()
    elif(n is "6"):
        exit()
    else:
        print("Invalid input")
