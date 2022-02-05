import json
import time
from threading import Thread
from channels.generic.websocket import WebsocketConsumer
class BoardConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    def disconnect(self, close_code):
        pass
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
        'message': message
        }))
        t = Thread(target=self.sendParallel)
        t.start()
    def sendParallel(self):
        time.sleep(3)
        self.send(text_data=json.dumps({
        'message': "Egal"
        }))

