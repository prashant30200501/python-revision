def greet(name):
    print("Hello", name)

greet("Piyush")
greet("Rahul")
greet("Aman")






try:
    num = int(input())
    print(num)

except:
    print("jdsnkjnn")


file = open("python.txt","w+")

file.write("bjfdsvjfdsi")

file.seek(0)
content = file.read()
print(content)
file.close()

