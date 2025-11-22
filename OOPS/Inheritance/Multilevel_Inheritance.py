class GrandFather:
    def displayName(self):
        print('Grand Father method calling...')

class Father(GrandFather):
    def displayName(self):
        print('Father method calling...')
        super().displayName()

class Son(Father):
    def displayName(self):
        print('Father method calling...')
        super().displayName()
        

s=Son()
s.displayName()