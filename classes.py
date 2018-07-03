# This is to show an example of classes and OOP concepts, namely Inheritance 
# and Polymorphism, in Python.

# define a Parent class
class Parent:
	# define a Parent Method (this will be inherited by the Child class)
	def parentMethod(self):
		print "Parent Method Called!"

	# define an Our Method (this will be polymorphed by the Child class)
	def ourMethod(self):
		print "Our Method Called (in Parent)!"

# define a Child class. notice that the Child class is inheriting the Parent class through the
# use of parentheses
class Child(Parent):
	# define a only Child Method (the Parent class won't have access to this)
	def childMethod(self):
		print ("Child Method Called!")

	# define an Our Method to overwrite the Parent's
	def ourMethod(self):
		print "Our Method Called (in Child)!"

if __name__ == '__main__':
	# first test the Parent
	print "Parent Instance"
	p = Parent()
	p.parentMethod()
	p.ourMethod()

	# now, test the Child
	print "\nChild Instance"
	c = Child()
	c.parentMethod()
	c.childMethod()
	c.ourMethod()
