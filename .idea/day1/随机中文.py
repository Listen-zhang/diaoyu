import random

# print([chr(random.randint(97,122)) for _ in range(10)])
# print([random.randint(0,100) for _ in range(10)])
p= ""
w=""
i = 0
while True:
  i += 1
  w +=  chr(random.randint(97, 122))
  p +=  str(random.randint(0,9))
  if i==10:
      break

