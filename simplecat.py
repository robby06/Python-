# This script will be a simple file cat. It will read in a filename from the commandline, open
# the file, and print to standard out (the terminal) the contents of the file.

# here as need to import the sys module (library) to grab the commandline argument (argv)
import sys

# we will also put everything into a main function
def main():
	# grab the filename from the commandline and open the file. erroring out on two conditions.
	# one: invalid number of arguments, and two: file not found
	if 2 != len(sys.argv):
		# remember the program is one of the arguments, thus the minus 1
		print "wrong amount of arguments. needed 1 got %d" % (len(sys.argv) - 1)
		print "usage: python simplecat.py <filename>"
		return -1

	filename = sys.argv[1]
	print "attempting to open " + filename

	# (just wanted to show you exception handling)
	try:
		inFile = open(filename, "r")
	except IOError:
		print "cannot open %s. are you sure it exists?" % filename
		return -1

	print "opened! here are the contents:"
	print "" #newline

	# the power of iterative for loops (side note: strip is a member function of the string
	# class. I'm striping the newlines because it stacks on top of the implicit newline of
	# the "print" function, and it makes the output annoyingly double spaced)
	for line in inFile:
		print line.strip('\n')

	# let's clean up and exit
	inFile.close()
	return 0

if __name__ == "__main__":
	main()
