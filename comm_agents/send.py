#communicating agent

import spade

class MyAgent(spade.Agent.Agent):
	class InfoBehaviour(spade.Behaviour.OneShotBehaviour):
		def _process(self):
			# first create the reciever
			recievers = spade.AID.aid(name = "recieve@127.0.0.1", addresses = ["xmpp://recieve@127.0.0.1","xmpp://recieve@10.42.0.189:8008"])
			# construct the message
			self.msg = spade.ACLMessage.ACLMessage()
			self.msg.setPerformative("inform")
			self.msg.addReceiver(receivers)
			self.msg.setContent("Hello World")
			# send the message
			self.myAgent.send(self.msg)

			print "Sender has sent a message:"

	def _setup(self):
		print "MyAgent starting . . ."
		b = self.InfoBehaviour()
		self.addBehaviour(b, None)

if __name__ == "__main__":
	a = MyAgent("comm@127.0.0.1", "secret")
	a.start()