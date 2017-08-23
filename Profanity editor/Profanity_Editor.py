import urllib.request
def Readfile():
    quotes=open(r"C:\Users\manis\Desktop\Python\movie_quotes.txt")
    filecontent=quotes.read()
    print(filecontent)
    quotes.close()
    Profanitycheck(filecontent)

def Profanitycheck(text):
    connection=urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output=connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!!")
    else:
        print("Could not scan document properly")


Readfile()
