#HackerRank 30 days of Code

class Solution:
    # Write your code here
    def __init__(self):
        self._stack = []
        self._queue = []
    
    def pushCharacter(self, data):
        self._stack.append(data)
        
    def popCharacter(self):
        return self._stack.pop()
    
    def enqueueCharacter(self, data):
        self._queue.append(data)
        
    def dequeueCharacter(self):
        return self._queue.pop(0)

# read the string s
s=raw_input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l / 2):
    print obj._stack, obj._queue
    stack = obj.popCharacter()
    queue = obj.dequeueCharacter()
    print stack, queue
    if stack != queue:
        print 'got here'
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
print isPalindrome
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")  