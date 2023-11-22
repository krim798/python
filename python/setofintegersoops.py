class setofint(object):
    def __init__(self):
        self.val = []
    def insert(self,i):
        if not i in self.val:
            self.val.append(i)
    def member(self,i):
        if i in self.val:
            return True
        else:
            return False
    def remove(self,i):
        try:
            self.val.remove(i)
        except Exception as ex:
            print(ex)
    def __str__(self):
        self.val.sort()
        result=''
        for i in self.val:
            result+=str(i)+', '
        return '{'+result[:-1]+'}'
    def intersect(self,other):
        commonvalueset=setofint()
        for val in self.val:
            if other.member(val):
                commonvalueset.insert(val)
        return(commonvalueset)
    def __len__(self):
        return len(self.val)
        
 # Testing the class
if __name__ == "__main__":
        s=setofint()
        s.insert(5)
        s.insert(3)
        s.insert(3)
        s.insert(7)
        s.insert(20)
        s.insert(-4)
        print("s=",s)
        print("member 5?",s.member(5))
        print("member -6?",s.member(-6))
        s.remove(5)
        s.remove(-6)
        print("after removing 5 from s, s=",s)
        \
        
