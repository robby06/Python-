#!/usr/bin/python

# This will be a tutorial in lists. Adding, remove, slicing, and dicing. This will also be a
# straight script. No functions here. Notice it also has the "she-bang" open which means it
# can be run independently. so, instead of "python allaboutlist.py", it can be ran (on Linux)
# ./allaboutlists.py (make sure it has the correct permissions!)

# let's create an empty list
a_list = []

# now, loop through and populate is with numbers
for i in range(0, 10):
	print "adding " + str(i)
	a_list = a_list + [i]
	print "new list: " + str(a_list)
	
# let's do the loop again, but instead of a 0-based numbering system let's make it a 1-based
# numbering system
for i in range(0, 10):
	a_list[i] = a_list[i] + 1

print "corrected list: " + str(a_list)

# now, we'll show off some slicing
print "beginning of the list to the fourth element: " + str(a_list[:5])
print "from the third element in the list to the end: " + str(a_list[3:])
print "from the second element of the list to the seventh: " + str(a_list[2:8])

# let's remove some elements from the end, and then show and count what's left
for i in range(0,4):
	x = a_list.pop()
	print "removing " + str(x)
print "new list: " + str(a_list) + " with " + str(len(a_list)) + " elements"

# let's append some things NOT integars
a_list.extend([True])
a_list.extend(["red"])
a_list.extend(['y'])

# now the current list
print str(a_list)

# let's delete the list and try to print it again. (this will fail)
del a_list
print str(a_list)


 
