#Tells program to take in all arguments
from sys import argv
#Assigns prompt line inputs variable names
script, filename = argv
#Creates variable txt to be the opening of sample filename
txt = open(filename)
#prints open read file of text file in txt
print "Here's your file %r" % filename
print txt.read()
#Does the same thing as before using raw_input instead of argv
print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()

txt.close()
txt_again.close()
