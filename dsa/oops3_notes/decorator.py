from datetime import date

def logger(fun):
    def wrapper():
        
        print("function::",fun.__name__,end=" ")
        print(date.today())
        fun()
        
    return wrapper

# m1
@logger
def doBackup():
    print("backup completed::")
    
# m2
doBackup = logger(doBackup)    
    
doBackup()