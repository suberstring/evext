import math

class DataTable:
	def __init__(self,head,value=[]):
		self.head = head
		self.value = value
		if type(self.head) != type([1]):
			raise TypeError("Error type,:(,please input a list like \"evext.DataTable([1,2,3])\".")

	def add_item(self,adder):
		if len(adder) != len(self.head):
			raise IndexError("Error size of two lists,:(.")
		self.value.append(adder)

	def delete_item(self,name):
		flag=-1
		for i in value:
			if i[0] == name:
				value.remove(i)
				flag=1
		return flag

	def to_list(self):
		return value

	def show_itself(self):
		for i in self.head:
			print(i,end=" ")
		print(" ")
		for i in self.value:
			for j in i:
				print(j,end=" ")
			print(" ")
class List:
	def __init__(self,value):
		self.value = value
		if type(value) != type([1]):
			raise TypeError("Error type,:(,please input a list like \"evext.List([1,2,3])\".")

	def add(self,val):
		self.value.append(val)
		return value
	def delete_by_number(self,nu):
		del self.value[nu]

	def delete_by_value(self,vl):
		self.value.remove(vl)

	def len(self):
		return len(self.value)

	def value_to_np_array(self):
		import numpy as np
		self.value=np.array(self.value)

	def sort(self):
		self.value = sorted(self.value)
		return sorted(self.value)

class Stack:
	def __init__(self,max_size="Infinity",value=[]):
		self.value=value
		self.max_size = max_size
	def push_in(self,val):
		if self.max_size == "Infinity" or len(self.value) < self.max_size:
			self.value.append(val)
		else:
			raise IndexError("Cannot use function \"push_in()\" in a full stack.:(")
	def push_back(self):
		if len(self.value) == 0:
			raise IndexError("Cannot use function \"push_back()\" in an empty stack.:(")
		del self.value[-1]
	def clear(self):
		self.value = []

class Dictionary:
	def __init__(self,value):
		self.value = value
		if type(value) != type({}):
			raise TypeError("Error type,:(,please input a dictionary like \"evext.Dictionary({1:2})\".")

	def all_key(self):
		ans=[]
		for i in self.value.keys():
			ans.append(i)
		return ans

	def all_value(self):
		ans=[]
		for i in self.value.values():
			ans.append(i)
		return ans

	def get_all(self):
		return self.value.items()

	def launch(self):
		a = list(self.value.keys())
		b = list(self.value.values())
		a.append(b)
		return a

def add(a,b):
	if type(a) != type([1]) and type(b) != type([1]):
		raise TypeError("Error type,:(,please input two lists like \"evext.add([1,2,3],[4,5,6])\".")
	if len(a) != len(b):
		raise IndexError("Error size of two lists,:(.")
	end=[]
	for i in range(0,len(a)):
		end.append(a[i]+b[i])
	return end

def sub(a,b):
	if type(a) != type([1]) and type(b) != type([1]):
		raise TypeError("Error type,:(,please input two lists like \"evext.add([1,2,3],[4,5,6])\".")
	if len(a) != len(b):
		raise IndexError("Error size of two lists,:(.")
	end=[]
	for i in range(0,len(a)):
		end.append(a[i]-b[i])
	return end

def mul(a,b):
	if type(a) != type([1]) and type(b) != type([1]):
		raise TypeError("Error type,:(,please input two lists like \"evext.add([1,2,3],[4,5,6])\".")
	if len(a) != len(b):
		raise IndexError("Error size of two lists,:(.")
	end=[]
	for i in range(0,len(a)):
		end.append(a[i]/b[i])
	return end

def div(a,b):
	if type(a) != type([1]) and type(b) != type([1]):
		raise TypeError("Error type,:(,please input two lists like \"evext.add([1,2,3],[4,5,6])\".")
	if len(a) != len(b):
		raise IndexError("Error size of two lists,:(.")
	end=[]
	for i in range(0,len(a)):
		end.append(a[i]/b[i])
	return end

def factorial(end,start=1):
	ans=1
	for i in range(start,end+1):
		ans*=i
	return ans

def array_function(func="sin",nm=10,start=0,spac=1):
	ed = []
	for i in range(start,start+nm+1):
		if func == "sin":
			ed.append(math.sin(i))
		elif func == "tan":
			ed.append(math.tan(i))
		elif func == "cos":
			ed.append(math.cos(i))
		else:
			raise NameError("No math function name like \""+func+"\" ,or we haven't add this function yet. :)")

	return ed


