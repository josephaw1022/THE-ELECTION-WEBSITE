#Automate file making and changes
# Joseph Whiteaker
# Made: 10/29/2020
# Last edited: 10/29/2020

##############################################################################################################################################################################
from os import system as terminal
def clear():
     terminal('clear')

def change(filename, content, mode="w+"):
    filename+=".html"
    file = open(filename,mode)
    file.write(content)

from page_content_holder import *
def format(content,filename="*"):
    global top
    global bottom
    file=open(filename,"w")
    file.write(top)
    file.write(content)
    file.write(bottom)

from os import listdir
directory = listdir('/Users/joseph/Desktop/Web Design Project/')


for i in range(len(directory)):
    if ("lab" not in directory[i]) and (".html" in directory[i]) and ("Lab" not in directory[i]) and ("hack" not in directory[i]):
        format(add_content,directory[i])



format(home_content,"index.html")
format(not_done_content,"not_done.html")
format(Candidates_content,"Candidates_content.html")
format(House_Results,"houseresults.html" )
format(senate_content,"senateresults.html")
format(senate_candidates,"senate_candidates.html")
format(my_rep,"myrep.html")
format(sources,"sources.html")
