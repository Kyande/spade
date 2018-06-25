import spade
import time

# host = "127.0.0.1"


class MyAgent(spade.Agent.Agent):
		
    class SendMsgBehav(spade.Behaviour.Behaviour):

        def _process(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("inform")
            msg.addReceiver(spade.AID.aid("rec",["xmpp://rec@127.0.0.1"]))
            msg.setContent("testSendMsg")

            self.myAgent.send(msg)
            
            print "Sender has sent a message:"
            print str(msg)

            time.sleep(1)

    def _setup(self):
        self.addBehaviour(self.SendMsgBehav())
        print "Sender started!"        

if __name__ == "__main__":
    a = MyAgent("communication@127.0.0.1", "secret")
    a.start()