import spade

class MyAgent(spade.Agent.Agent):
	"""base agent class"""
	class Behav(spade.Behaviour.PeriodicBehaviour):
		"""behaviour class for the Agent"""
		def onStart(self): # instantiate agent.
			print "Starting behaviour..."
			self.counter = 0

		def _onTick(self): # repeat printing count and increment counter.
			print "Counter: ", self.counter
			self.counter = self.counter + 1

	def _setup(self):
		""" Instantiate agent class """
		print "Starting agent...."
		b = self.Behav(1) 
		self.addBehaviour(b, None) # add behaviour to agent.

if __name__ == '__main__':
	a = MyAgent("period@127.0.0.1", "secret")
	a.start()
			
