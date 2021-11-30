def capitalize_sentences(x):
    y=""
    if(x[0]!=('.', '?', '!', ' ')):
        y+=x[0].upper()
    for i in range(1,len(x)):
        if((x[i-2]=='.' or x[i-2]=='?' or x[i-2]=='!' )and x[i-1]==' '):
            if(i<(len(x)-3)):
                y+=x[i].upper()
            else:
                y+=x[i]
        else:
            y+=x[i]
    return y
