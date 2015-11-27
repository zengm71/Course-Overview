import sys
print(sys.argv)

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Enter your name: ")

for i in range(len(name), 0, -1):
    print( name[0:i], end = " ")
    for j in range(i,len(name)):
        print(" "* 2*(j-i) + name[j], end = "")
    print("")
