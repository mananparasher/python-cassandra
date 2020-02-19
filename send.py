curl --header "Content-Type: application/json" --request POST --data \
'{"event": "start","country": "FI","player_id": "0a2d12a1a7e145de8bae44c0c6e06629","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d4","ts": "2016-12-02T12:48:05.520022"\}' 
http://127.0.0.1:5000/session



 curl localhost:5000/session -d '{"event": "start","country": "FI","player_id": "0a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d4","ts": "2016-12-02T12:48:05.520022"}' -H 'Content-Type: application/json'




 curl localhost:5000/receiving -d '{"event": "end","player_id": "0a2d12a1a7e145de8bae44c0c6e06633","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d4","ts": "2016-12-02T12:48:05.520022"}' -H 'Content-Type: application/json'




 curl localhost:5000/twenty_complete_sessions -d '{"player_id": "0a2d12a1a7e145de8bae44c0c6e06633"}'



curl localhost:5000/receiving -d '{"event": "start","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d4","ts": "2019-12-02T12:48:05.520022"}' -H 'Content-Type: application/json'

curl localhost:5000/receiving -d '{"event": "end","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d4","ts": "2019-12-02T12:49:05.520022"}' -H 'Content-Type: application/json'



curl localhost:5000/receiving -d '{"event": "start","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d5","ts": "2016-12-02T12:48:05.520022"}' -H 'Content-Type: application/json'

curl localhost:5000/receiving -d '{"event": "end","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d5","ts": "2016-12-02T12:49:05.520022"}' -H 'Content-Type: application/json'


curl localhost:5000/receiving -d '{"event": "start","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d6","ts": "2016-12-02T12:48:05.520022"}' -H 'Content-Type: application/json'

curl localhost:5000/receiving -d '{"event": "end","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d6","ts": "2016-12-02T12:49:05.520022"}' -H 'Content-Type: application/json'



curl localhost:5000/receiving -d '{"event": "start","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d7","ts": "2016-12-02T12:48:05.520022"}' -H 'Content-Type: application/json'

curl localhost:5000/receiving -d '{"event": "end","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d7","ts": "2016-12-02T12:49:05.520022"}' -H 'Content-Type: application/json'



curl localhost:5000/receiving -d '{"event": "start","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d8","ts": "2016-12-02T12:48:05.520022"}' -H 'Content-Type: application/json'

curl localhost:5000/receiving -d '{"event": "end","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d8","ts": "2016-12-02T12:49:05.520022"}' -H 'Content-Type: application/json'



curl localhost:5000/receiving -d '{"event": "start","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d9","ts": "2016-12-02T12:48:05.520022"}' -H 'Content-Type: application/json'

curl localhost:5000/receiving -d '{"event": "end","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d9","ts": "2016-12-02T12:49:05.520022"}' -H 'Content-Type: application/json'


curl localhost:5000/receiving -d '{"event": "start","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d10","ts": "2016-12-02T12:48:05.520022"}' -H 'Content-Type: application/json'

curl localhost:5000/receiving -d '{"event": "end","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d10","ts": "2016-12-02T12:49:05.520022"}' -H 'Content-Type: application/json'



curl localhost:5000/twenty_complete_sessions -d '{"event": "end","country": "FI","player_id": "a2d12a1a7e145de8bae44c0c6e06632","session_id":"4a0c43c9-c43a-42ff-ba55-67563dfa35d10","ts": "2016-12-02T12:49:05.520022"}' -H 'Content-Type: application/json'


