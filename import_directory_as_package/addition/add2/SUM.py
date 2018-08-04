class Add:
	ans=0
	def __init__(self):
		self.reset()
		pass
	def sum(self,*args):
		sol=0
		[ self._addition(i) for i in args]
		return self.ans
	def _addition(self,i):
		self.i=i
		self.ans=self.ans+self.i
	def reset(self,a=0):
		self.ans=a
