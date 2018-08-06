'''class ADD ,having method __init__ , sum _addition,reset ''' 
class Add:
	''' in this add variable all sum data is stored . '''
	ans=0	
	
	'''initizing a object without any argument  __init__ function . ie x=Add()  
	no argument is used in Add() .'''
	
	def __init__(self):		
		'''set value of ans to 0 each time when object is callled ADD.'''
		self.reset()
		pass
	
	''' gives value to add to function  any no of values
	eg   x.sum(1,2,3,4) or x.sum(1,2,3,4,5,6,7,8,9) .
	no resetriction on input values. 
	.to see how this happenes see *args property in python. '''
	
	
	def sum(self,*args):
	    ''' for faster excecution .this is functioning same as 
	            for i in args:
	                self.addition(i)
	    but used method is much faster than above one which isusing for loop.
	    see list comprehension  for details.
	    '''
	    [ self._addition(i) for i in args]
	    return self.ans  
	    '''giving the value of ans variable .ie total sum of input. '''
	
	def _addition(self,i):
		
		''' getting the value form self._addition(i) each time this is called and
		storing it in the ans variable . '''
		
		
		self.i=i
		self.ans=self.ans+self.i
		
		
		
	'''setting value of ans to 0 each time it is called '''	
	def reset(self) : 
		self.ans=0
		
