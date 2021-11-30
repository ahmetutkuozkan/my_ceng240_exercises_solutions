def health_bar(x,y,z):
    health=y-z
    if(health<0):
        health=0
    result="X"*health+"_"*(x-health)
    return result
