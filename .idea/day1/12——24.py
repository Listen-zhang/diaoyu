
i = 0
def a():
   while True:
    global i
    i+=1
    if i == 10:
        break
    yield  i

f  =a()
print(type(f))
while True:
    print(next(f))