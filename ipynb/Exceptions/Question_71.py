class MyError(Exception):


    def __init__(self,msg):
        self.msg = msg


e = MyError("something wrong")
print(e)