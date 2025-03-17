x = "KIA"

print(type(x))

def myfunc():
    x = "MERCEDES"
    global y
    y = 5
    print(type(y))
    print("I want to drive a " + x)

myfunc()
print("My dad drove a", x)

#f-strings provide a clean way to embed expressions inside string literals. When you use curly braces {}, Python automatically converts the value to a string. This is the recommended approach for modern Python code.
print(f"At a point, he had over {y} cars that I knew off")
txt = "Not at the same I guess"
if "the" in txt:
    print (txt)

#this prints between a range of index in a strings, note the first character is index '0'
t = "Bro this guy sucks"
print(t[3:10])

#slice from the start
print(t[:15])

#slice to the end 
print(t[4:])

x = "Welcome"
print(x[0:7])

#upper() for uppercase, lower() for lowercase
print(x.upper())

print(x.lower())


V = 700
print(f"I'm trying to see how this works exactly the price is {700} dollars")