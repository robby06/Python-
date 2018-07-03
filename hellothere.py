# This is a simple python script to get data from a user,
# and repeat it back to stdout.

def helloThere():
	# a simple retrieve and repeat
	name = raw_input("What is your name? ")
	print("Hello there, " + name + ". How are you today?")
	
	# let's do a bit more!
	print "\nI can add numbers for you!"
	first = input("Pick the first one: ")
	second = input("Pick the second one: ")
	
	# convert the strings to ints
	first = int(first)
	second = int(second)
	
	# let's try the C style of print (remember the variables must be 
	# sent as a tuple)
	print "%d + %d = %d" % (first, second, (first + second))
	
	# say goodbye and leave
	print "\nGoodbye!"

	
	return 0

if __name__ == '__main__':	
	helloThere()
