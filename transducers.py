import functools

#http://phuu.net/2014/08/31/csp-and-transducers.html
#http://habrahabr.ru/post/237613/
#http://habrahabr.ru/post/237733/


#TODO: Replace functools.reduce to original step function
def flatten():
	def step(s):
		def items(result, item):
			for i in range(0, len(item)):
				result = step(result, item[i])
			return result



class Reduced:
	def __init__(self, wrapped):
		self._wrapped = wrapped

	def unwrapped(self):
		return self._wrapped

def TTake(num):
	def step(s):
		count = 0
		return functools.reduce(lambda x,y: step(x) if count < num else Reduced(x),s,[])
	return step([1,4,5,8,9])


class TFunc:
	def __init__(self, transform):
		self.transform = transform
	
	def fit(self, coll):
		pass

	def _app(self, x,y):
		x.append(y)
		return x

class TMap(TFunc):
	def __init__(self, transform):
		TFunc.__init__(self, transform)

	def fit(self, coll):
		return functools.reduce(lambda x,y: self._app(x,self.transform(y)), coll, [])

class TFilter(TFunc):
	def __init__(self, compare):
		TFunc.__init__(self, compare)

	def fit(self, data):
		return functools.reduce(lambda x,y: self._app(x,y) \
			if self.transform(y) else x, data, [])

#TODO
class TTakeWhile(TFunc):
	def __init__(self, transform):
		TFunc.__init__(self, transform)

	def fit(self, data):
		pass

class Compose:
	def __init__(self, *args):
		self.funcs = args

	def run(self, data):
		result = data
		for f in self.funcs:
			result = f.fit(result)
		return result

class Reduced:
	''' In the termination case '''
	def __init__(self):
		pass

def transducer(start, funcs, data):
	if len(data) == 0:
		raise Exception("Data not contain any elements")

	return funcs.run(data)
