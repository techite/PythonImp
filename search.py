# This code helps you execute search queries on Google using Python terminal
menu={}
menu[1]="Google"
menu[2]="Yahoo"
menu[3]="Dogpile"
menu[4]="DuckDuckGo"
menu[5]="Ecosia"
menu[6]="Exit()"
print "#################################"
print " Choose Search Engine - > Fire Query"
print " By Shashi Prakash Agarwal" 
import webbrowser
while True:
    options=menu.keys()
    options.sort()
    for entry in options:
        print entry, menu[entry]
    selection=raw_input("Select Engine No:")
    search_query=raw_input("Enter Search Query:")
    if selection =='1':
        webbrowser.open('http://google.com/search?q='+search_query)
    elif selection == '2':
        webbrowser.open('http://yahoo.com/search?p='+search_query)
    elif selection == '3':
        webbrowser.open('http://dogpile.com/search/web?q='+search_query)
    elif selection == '4':
        webbrowser.open('http://duckduckgo.com/?q='+search_query)
    elif selection == '5':
        webbrowser.open('http://ecosia.com/search?q='+search_query)
    elif selection == '6':
        print "Bye Bye!"
        break
    else:
        print "Unknown Option Selected!"
