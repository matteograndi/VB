from sys import argv
import string

# The maximun words combination
MAX_WORD = 5
MIN_WORD = 1
TOP_LIST = 20

file_used = "File.txt"


sentence = '"%s" - a %d word phrase which is in the result with the weight %d (occurred %d times)'


def ReadText(File):
    try:
        f = open(File,"r")
    except: 
         print "File not exist!!"
         raise   
    text = ""
    while (1):
        app = f.read(50)
        text = text + app.replace("\n"," ")
        if app=="":
            break
    f.close()
    return text
    

def CleanWord(app):
    # function that delete all of the character of punctuation
    # of a string
    leng = len(app)
    for i in range(0, leng):
        if ('A' <= app[i] <= 'z') or ('a' <= app[i] <= 'z') or ('1' <= app[i] <= '9'):
            pass
        else:
            if app[i]!= " ":
                # if the next character the ' is a 's' or a 'd' i delete it
                if app[i] == "'" and (app[i+1]=='s' or app[i+1]=='d' ):
                    app = app[:i+1] + "+" + app[i+2:]
                # if I have 've I delete it
                if app[i] == "'" and (app[i+1]=='v' and app[i+2]=='e' ):
                    app = app[:i+1] + "++" + app[i+3:]
                app = app[:i] + "+" + app[i+1:]
    app = app.replace("+", "")
    app = app.replace("  "," ")
    return app
                

def Take_Val():
    # little function 
    c = 0
    val = -1
    while c == 0:
        try:
          print "Would you:\n1) Insert a name of an existing file\n2) Use the program with the file 'File.txt'"
          val = input("choice: ")
          if 0 < val <= 2 :
              c = 1
          else:
              print "You must specify the 1 or 2 choice\n"
        except:
            print "You've insert a wrong choice!!!\n"
    return val


def CountWord(text):
    counter = {}
    #text1 = text
    for i in range(MIN_WORD, MAX_WORD + 1):
        text1 = text
        
        while (text1 != ""):
            # scroll the text 
            app = 0
            word = ""
            text2 = text1
            for j in range(0,i):
                # search a single/group_of words
                app = text2.find(" ")
                if app == -1:
                    # the text is finished 
                    break;
                word = word + text2[:app]
                # little control to make the " " beetwen two word 
                # in the case I search a sequence of two words
                if j < i-1:
                    word = word + " "
                text2 = text2[app+1:]
                # in text1 I MUST remove ONLY the first word
                if j == 0:
                    text1 = text2
            
            # if the test is not finished
            if app != -1:
                # print word
                # I put all the occurring that I've found
                # in a dictionary
                if word != "":
                    if word in counter.keys():
                        counter[word] = counter[word] + 1
                    else:
                        counter[word] = 1

    return counter

def CountCharacter(text, c):
    # is a simply function that return the occurring of a character
    cont = 1
    for char in range (0,len(text)):
        if text[char] == c:
            cont += 1
    return cont


if __name__ == "__main__":
    
    choice = Take_Val()
    if choice == 1:
        print "Insert the name of file: ",
        fi = raw_input()
        text = ReadText(fi)
    if choice == 2:
        text = ReadText(file_used)
    

    # Clean the word from the other punctuation 
    text = CleanWord(text)
    
    # create the counter
    counter = CountWord(text)
    #print counter
    
    
    
    # find the max occurring
    max = 0
    tot = 0
    for i in counter:
        if counter[i] > max:
            max = counter[i]
        tot += 1
    
    for i in range(0, 3): 
        print 

    # I use tot because I could have a short file with 2 words
    # so it is impossible to find 20 occurrence
    if TOP_LIST > tot:
        n = tot
    else:
        n = TOP_LIST
   
 
    
    listcounter = counter.items()
    listcounter1 = []
    for lc in listcounter:
        word_number = CountCharacter(lc[0], " ")
        listcounter1.append([lc[1],word_number,lc[0]])
 
    listcounter1.sort()
    lenght = len(listcounter1)
    #print listcounter1
    for i in range(0,n):
        lc = listcounter1[lenght-i-1]
        #print lc
        print sentence % (lc[2], lc[1], lc[1] * lc[0], lc[0])
 
        
