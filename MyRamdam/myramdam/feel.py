from dosql import doSql 

class Feel(object):

	def __init__(self):
		True
		
	def get_feeling(self, feel_id):
		x = doSql()
		ans = x.execqry("select * from get_feeling(" + feel_id + ");", False)

		return ans

	def add_feeling(self, feeling1):
		x = doSql()
		ans = x.execqry("select * from add_feeling('" + feeling1 + "');", True)
		return ans
		