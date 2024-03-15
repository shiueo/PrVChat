import json
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol


class AESCipher:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, iv=get_random_bytes(AES.block_size))
        return cipher.iv + cipher.encrypt(raw)

    def decrypt(self, enc):
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


class ChatProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.clients.append(self)
        print("Client connected")

    def dataReceived(self, data):
        try:
            data = json.loads(data)
            if 'message' in data:
                print(data['name'] + ": " + self.factory.cipher.decrypt(data['message']).decode())
        except Exception as e:
            print("Error:", e)

    def sendMessage(self, message):
        for client in self.factory.clients:
            client.transport.write(json.dumps({
                'name': self.factory.name,
                'message': self.factory.cipher.encrypt(message.encode())
            }).encode())


class ChatFactory(Factory):
    def __init__(self, name):
        self.clients = []
        self.name = name
        self.cipher = AESCipher("your_secret_key")

    def buildProtocol(self, addr):
        return ChatProtocol(self)


if __name__ == "__main__":
    name = input("Enter your name: ")
    reactor.listenTCP(8000, ChatFactory(name))
    endpoint = TCP4ClientEndpoint(reactor, "localhost", 8000)
    d = connectProtocol(endpoint, ChatProtocol(ChatFactory(name)))
    d.addCallback(lambda p: p.sendMessage("Hello, world!"))
    reactor.run()
