"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy():
    def __init__(self):
        self.items = []
        
    def getClassiness(self):
        total = 0
        dic = {"tophat" : 2,"bowtie" : 4,"monocle" : 5 }
        for i in dic:
            variable = self.items.count(i) * dic[i]
            total += variable
        return total
    def addItem(self,a):
        self.items.append(a)
        
    
            

# Test cases
me = Classy()

# Should be 0
print (me.getClassiness())

me.addItem("tophat")
# Should be 2
print (me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print( me.getClassiness())

me.addItem("bowtie")
# Should be 15
print( me.getClassiness())