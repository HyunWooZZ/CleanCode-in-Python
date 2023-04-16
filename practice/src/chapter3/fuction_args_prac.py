def fuction(args):
    args += " in fuction"
    print(args)

immutable = "hello"
fuction(immutable)

mutable = list('hello')
fuction(mutable)

# when we don`t want to change the mutable object but when we print the mutable
# the mutable object is changed...

print(immutable)
print(mutable)

test = ["string"]
test += list("temp")

print(test)
