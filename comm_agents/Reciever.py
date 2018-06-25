import spade

# host = "127.0.0.1"

class MyAgent(spade.Agent.Agent):
    
    class RecvMsgBehav(spade.Behaviour.Behaviour):

        def _process(self):
            msg = self._receive(block=True,timeout=10)
            print "client has received a message:"
            print str(msg)
    
    def _setup(self):
        # template = spade.Behaviour.ACLTemplate()
        # template.setSender(spade.AID.aid("communication@127.0.0.1",["xmpp://communication@127.0.0.1"]))
        # t = spade.Behaviour.MessageTemplate(template)
        # self.addBehaviour(self.RecvMsgBehav(),t)
        rb = self.RecvMsgBehav()
        self.setDefaultBehaviour(rb)

	print "Receiver started!"
if __name__ == '__main__':
	b = MyAgent("rec@127.0.0.1", "secret")
	b.start()		