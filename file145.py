class student:
    def __init__(self,name,branch):
        print('constructor executed..')
        self.name = name
        self.branch = branch
    def details(self):
        print('hello:',self.name)
        print('branch:',self.branch)
        print('method execution..')
