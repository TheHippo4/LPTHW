from sys import argv

script, filename = argv

txt = open(filename)
print txt.read()

file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
txt_again.close()
