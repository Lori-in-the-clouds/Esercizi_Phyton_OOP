class CaseString:
    def __int__(self,st,upper = False):
        self.st = st
        self.upper = upper

    def set_upper(self,upper):
        self.upper = upper

    def set_string(self,st):
        self.st = st
    def get_string(self):
        if self.upper == True:
            return self.st.upper()
        else:
            return self.st

