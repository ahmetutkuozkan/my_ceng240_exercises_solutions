encoding_words = input()
a=0
result=""
letter=""
letter=encoding_words[0]
for i in range(0,len(encoding_words)):

    if(letter==encoding_words[i]):
        a+=1
        if(len(encoding_words)==(i+1)):
            result+=str(a)+letter


    else:
        result+=str(a)+letter
        a=1
        letter=encoding_words[i]
        if(len(encoding_words)==(i+1)):
            result+=str(a)+letter




print(result)
