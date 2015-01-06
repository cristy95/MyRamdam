from dosql import *
import cgi

class NewFeel(object):
    
    def addFeel(req,newfeelname):
        newfeelname= cgi.escape(newfeelname)

        a = doSql()
        
        rets = x.execqry("select add_custfeel('" + newfeelname + "');",True)
        result = []
        
        for ret in rets:
            stringed = map(str, ret)
            result.append(stringed)

        return result

    def getLeanFeel(req, newfeelname):
    	newfeelname = cgi.escape(newfeelname)

    	a = doSql()

    	rets = x.execqry("select get_leanfeel('" + newfeelname + "');",False)
        result = []
        
        for ret in rets:
            stringed = map(str, ret)
            result.append(stringed)

        return result

    