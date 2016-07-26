from spark.rooms import Room
from spark.messages import Message
from spark.session import Session

token =  'Put Your Auth Token Here'
roomname = 'DevOps Forum IoT'

url = 'https://api.ciscospark.com'

session = Session(url, token)

message = Message()
room = Room.get(session, name=roomname)
message.text = 'Put your message here'
room.send_message(session, message)

