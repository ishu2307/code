class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.head
            self.head=newnode
    def insertatend(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            self.tail.next=newnode
            self.tail=newnode
    def insertatpos(self,position,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            temp=self.head
            for i in range(1,position-1):
                temp=temp.next
            newnode=Node(value)
            newnode.next=temp.next
            temp.next=newnode
            temp=None

    def delatbeg(self):
        if(self.head==None):
            print("Empty List")
        else:
            temp=self.head
            self.head=temp.next
            temp=None

    def delatend(self):
        if(self.head==None):
            print("Empty List")
        else:
            temp=self.head
            while(temp.next is not None):
                prev = temp
                temp = prev.next
            self.tail=prev
            self.tail.next=None

    def delatpos(self,key):
        if(self.head==None):
            print("Empty List")
        else:
            count=0
            temp=self.head
            while(temp.data is not key):
                count=count+1
                if(temp.next is not None):
                    prev = temp
                    temp = prev.next
                else:
                    print("**Value to be deleted is not found**")
                    break
            if(count is not 0):
                prev.next=temp.next
            else:
               print("You are trying to delete the first value in the list,so kindly go for option 1 in deletion menu")
            temp=None 
            prev=None

    def searching(self,key):
        val=input()
        if(self.head==None):
            print("Empty List")
        else:
            temp=self.head
            while(temp.data is not key):
                if(temp.next is not None):
                    prev = temp
                    temp = prev.next
                else:
                    print("Value is not found:(")
                    break
            else:
                print("Value is found:)")
            temp=None

    def updating(self,oldv,newv):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.data is not oldv):
                if(temp.next is not None):
                    temp=temp.next
                else:
                    print("Value is not found in the list")
                    break
            else:
                temp.data=newv
            temp=None

    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

s=SLL()
print("****Welcome to Singly linked list***")
while(True):
    print("Operations")
    print("*select required option*")
    print("1. Insertion")
    print("2. Deletion")
    print("3. Searching")
    print("4. Updation")
    print("5. Display")
    print("6. Exit")
    n=input()
    if(n is "1"):
        print("where you want to insert the string?????")
        print("<<1. Insert at beginning>>")
        print("<<2. Insert at end>>")
        print("<<3. Insertion at any position between head and tail>>")
        n=input()
        if(n == "1"):
            print("Enter string to be inserted")
            val=input()
            s.insertatbeg(val)
        elif(n == "2"):
            print("Enter string to be inserted")
            val=input()
            s.insertatend(val)
        elif(n == "3"):
            print("Enter the position, where value to  inserted the string")
            pos=int(input())
            print("Enter string to be inserted")
            val=input()
            s.insertatpos(pos,val)
        else:
            print("Invalid input")
    elif(n == "2"):
        print("Where you want to delete the string")
        print("<<<1. Delet at beginning>>>")
        print("<<<2. Deletion at end>>>")
        print("<<<3. Deletion at any position between head and tail>>>")
        n=input()
        if(n == "1"):
            s.delatbeg()
        elif(n == "2"):
            s.delatend()
        elif(n == "3"):
            print("Enter string to be deleted")
            val=input()
            s.delatpos(val)
        else:
            print("Invalid input")
    elif(n == "3"):
        print("Enter string to be searched")
        s.searching(val)
    elif(n == "4"):
        print("Enter the old value")
        val=input()
        print("Enter the new value")
        val1=input()
        s.updating(val,val1)
    elif(n == "5"):
        s.display()
    elif(n == "6"):
        exit()
    else:
        print("Invalid input")
