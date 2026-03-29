class Solution(object):
    def reverseList(self, head):
        
        curr = head #Initialize curr to the head of linked list
        prev = None #Initialize prev to null/none

        while curr != None: #loop until curr is none, like prev is currently which will happen after reversing

            next_tmp = curr.next #save next, the node after curr
            curr.next = prev #set the pointer of curr to prev

            prev = curr #prev moves up 1 to curr
            curr = next_tmp #curr moves up 1 to next

        return prev #return prev because it is the new head of the reversed linked list
    
'''
This one was a little tough just because I kinda forgot how linked lists work and python but the actual logic is solid
'''