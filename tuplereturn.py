# This is an example of functions and returning multiple values via a tuple. This will also
# demonstrate how a docstring can be created and called.

def baseToAPower(base, power):
	'''
	baseToAPower(base, power)
		This function will take in a base number and raise it up to the incoming
		power variable. It will then return the base, power, and the result in a
		tuple for easy printablility.
	'''

	return (base, power, base ** power)

if __name__ == "__main__":
	# first, let's call the docstring
	print baseToAPower.__doc__

	# now, let's run the function a few times with print statements to make sure everything
	# is working. for added illustration, we will print using the three different types of
	# ways

	# concatenate print (str() is a built-in function like int() or float() since you can
	# only concatenate a string to a string)
	x, y, z = baseToAPower(2, 3)
	print str(x) + " to the " + str(y) + " is " + str(z)

	# comma delimited print (notice that with commas you don't need the space padding either
	# side in the string literals. Python takes care of that for you
	x, y, z = baseToAPower(4, .5)
	print x, "to the", y, "is", z

	# C-style print (in a C-style print the variable must be passed as a tuple itself)
	x, y, z = baseToAPower(10, 10)
	print "%d to the %d is %d" % (x, y, z)

