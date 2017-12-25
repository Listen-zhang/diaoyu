class Mylist:
    class Myn:
        def __init__(self):
            self.data=None
            self.next= None

    def __init__(self):
        self.haid=None
        self.l = None
        self.size=0
    def add(self,n):
      self.size+=1
      d =self.Myn()
      d.data = n
      if self.haid == None:
          self.haid=d
      else:
          self.l.next = d
      self.l = d
    def get(self,i):
        p = self.haid
        for i in range(0,i):
          p =  p.next
        return p.data
d= Mylist()
d.add("ee")
d.add("dd")
d.add("aa")
d.add("cc")
for i in range(0,d.size):
    print(d.get(i))

