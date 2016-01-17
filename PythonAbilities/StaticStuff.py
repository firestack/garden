import time
listoftest = []
def t(func):
        print "t(",func,')'
        listoftest.append(func)
        return func

class decTest:
        mList = []
        def __init__(self, func):
                try:
                        print "decTest.__init__(", self,',', func,')'
                except:
                        print func

        def __call__(self):
                print "decTest.__call__(",self,')'

       
        class table:
                def __getattr__(self, name):
                        return name

        tables = table()
        def printme(func):
                print "decTest.printme(",func,")"
                
    

class StaticClasObject(object):
        """docstring for StaticClasObject"""

        def __init__(self, arg):
                super(StaticClasObject, self).__init__()
                self.arg = arg
                
        var = "No init yet"



        @classmethod
        def change_var(self, new_var):
        	print "is classmethod"
        	print self
                self.var = new_var


class ExceptionTest(BaseException):
	"""docstring for ExceptionTest"""
	def __init__(self):
		super(ExceptionTest, self).__init__()


def testing():
        print "Hello world!"

@decTest
def readList():
        print listoftest

def test(**kwargs):
        return find(**kwargs)

def find(**kwargs):
        pairs = []
        for k,v in kwargs.items():
                if isinstance(v, list) or isinstance(v, tuple):
                    sub_querys = [k+'=\''+str(item)+'\'' for item in v]
                    pairs.append('('+" OR ".join(sub_querys)+')')

                else:
                    pairs.append(k+'=\''+str(v)+'\'')

        return "WHERE "+" AND ".join(pairs)

if __name__=="__main__":
        """
        print StaticClasObject.var
        StaticClasObject.change_var('')


        k = StaticClasObject('d')
        print k.var
        k.change_var("Changed?")

        print k.var
        print StaticClasObject.var

        #raise ExceptionTest
        """
        """
        #readList()
        l = decTest("hi      ")
        print l.tables.hi"""
        try:
                print time.time(),": Try...?"
                #raise TypeError
        except:
                print time.time(),": Except...?"
                #raise TypeError
        else:
                print time.time(),": Else...?"
                #raise TypeError
        finally:
                print time.time(),": Finally..."
                #raise TypeError
        print test(twitch_name=("bomb_mask", "batedurgonnadie"), user_id=5, k=50)

        try:
            while True:
                raise TypeError
        finally:
            print "Finally"