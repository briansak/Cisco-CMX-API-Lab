from spark.rooms import Room
from spark.session import Session

token =  'Put your Auth Token Here'

url = 'https://api.ciscospark.com'

session = Session(url, token)

room = Room()
room.title = 'DevOps Forum IoT'
room.create(session)
