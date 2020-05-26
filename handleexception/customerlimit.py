class OverTheLimitException(Exception):
    def __init__(self,msg):
        self.msg = msg
        
def withdrawl(amount):
    if(amount>500):
        raise OverTheLimitException('you cannot withdrawl more then 500')
    
    
withdrawl(501)    
                