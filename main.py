
class Main:

    def __init__(self):
        self.messages = []
        self.msgUsers = []

    def addMessage(self , message , userName):
        self.messages.append(message)
        self.msgUsers.append(userName)


    def getMessages(self):
        return self.messages

