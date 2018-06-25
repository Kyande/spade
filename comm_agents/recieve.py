# reciever agent.

import spade

class MyAgent(spade.Agent.Agent):
	""" base agent class """

	class RecieveBehav(spade.Behaviour.Behaviour):
		""" This behaviour recieves all messages """
		def _process(self):
			# Blocking.
			self.msg = self._receive(True)

			

	def _setup(self):
		""" instantiate agent class """

		#make RecieveBehav as default behaviour
		rb = self.RecieveBehav()
		self.setDefaultBehaviour(rb)

if __name__ == '__main__':
	a = MyAgent("recieve@127.0.0.1", "secret")
	a.start()	