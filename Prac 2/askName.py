name = input('Please enter your name')
f = open("name.txt",'w')
f.write(name)
f.close()