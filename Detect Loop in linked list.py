# Return boolean value True or False

class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # Agar list empty hai ya sirf ek hi node hai, toh loop possible nahi hai
        if head is None or head.next is None:
            return False

        # Do pointers lete hain — slow aur fast
        slow = head
        fast = head

        # Jab tak fast ya fast.next null nahi hota, loop check karte hain
        while fast and fast.next:
            slow = slow.next           # slow ek-ek step
            fast = fast.next.next      # fast do-do step

            # Agar slow aur fast kabhi mil gaye, toh loop hai
            if slow == fast:
                return True

        # Agar loop khatam ho gaya bina mile, toh koi loop nahi hai
        return False
