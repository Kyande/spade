# time out agent

import spade

class MyAgent(spade.Agent.Agent):
	"""docstring for MyAgent"""

	class MyBehav(spade.Behaviour.TimeOutBehaviour):

		def onStart(self):
			print "Starting Behaviour...."

		def timeOut(self):
		    print "The time out has ended...."

		def onEnd(self):
			print "Ending Behaviour...."    	
	
	def _setup(self):
		#inittalize agent and add behaviour
		print "Agent is Starting ..."
		b = self.MyBehav(5)
		self.addBehaviour(b, None)

if __name__ == '__main__':
	a = MyAgent("agent@thx1138.dsic.upv.es", "secret")
	a.start()