class Myb:
    class my_no:
        def __init__(self):
                self.data = None
                self.l = None
                self.r = None
        def add(self,n):
            if self.data >n.data:
                if self.l is  None:
                    self.l = n
                else:
                    self.l.add(n)
            if self.data<n.data:
                if self.r is  None:
                        self.r = n
                else:
                        self.r.add(n)
        def zhong(self):
            if self.l is not None:
                self.l.zhong()
            if self.r is not None:
                self.r.zhong()
            print(self.data)
    def __init__(self):
        self.root = None
    def add(self,data):
        n  = self.my_no()
        n.data  = data
        if self.root is None:
            self.root = n
        else:
            self.root.add(n)
    def zhong(self):
        self.root.zhong()

t = Myb()
t.add(10)
t.add(5)
t.add(11)
t.add(14)
t.zhong()
