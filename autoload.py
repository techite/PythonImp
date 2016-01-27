#Auto Load multiple URLs from a text file
#By Shashi Prakash Agarwal
import webbrowser
with open('a.txt') as f:
    for line in f:
        webbrowser.open(line)
#Ensure that a.txt exists and contains URLs separated by line break (i.e. one URL per line)
