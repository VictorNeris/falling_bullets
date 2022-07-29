import host

class timer(object):
	
	class once(object):

		def __init__(self, time, method, *args):
			self.time = host.timer_getWallTime() + time
			self.interval = 0
			self.alwaysTrigger = 1
			self.method = method
			self.args = args
			host.timer_created(self)

		def onTrigger(self):
			self.method(*self.args)
			self.abort()

		def abort(self):
			host.timer_destroy(self)
			
	class loop(object):

		def __init__(self, time, method, *args):
			self.__dict__['time'] = host.timer_getWallTime() + time
			self.interval = time
			self.alwaysTrigger = 1
			self.method = method
			self.args = args
			host.timer_created(self)

		def __setattr__(self, name, value):
			if name != "time":
				self.__dict__[name] = value

		def onTrigger(self):
			self.method(*self.args)
			self.__dict__['time'] += self.interval

		def abort(self):
			host.timer_destroy(self)