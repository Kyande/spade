import spade

class MyAgent(spade.Agent.Agent):
	"""Base class for my agent"""
	class Behav(spade.Behaviour.OneShotBehaviour):
		"""class declaring agent behavior"""
		#instantiate agent
		def onStart(self):
			print "Starting Behaviour...."

		def _process(self):
			print "Hello World from a one shot behaviour..."

		def onEnd(self):
			print "Ending Behaviour..."

	def _setup(self):
		print "Agent is Starting ..."
		b = self.Behav()
		self.addBehaviour(b, None)

if __name__ == '__main__':
	a = MyAgent("one@127.0.0.1", "password")
	a.start()
		
			