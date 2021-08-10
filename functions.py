def countWords():
    fileName=input('enter the file name')
    f=open(fileName,"r")
    count=0
    for i in f:
        word=i.split()
        count=count+len(word)
    print(count)
countWords()