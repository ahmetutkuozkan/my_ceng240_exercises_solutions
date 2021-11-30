slogan = input()
slogan = slogan[:(slogan.find('than')+2)] + "e" + slogan[(slogan.find('than')+3):]
print(slogan)

