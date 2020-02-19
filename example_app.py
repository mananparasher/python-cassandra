import json
from datetime import datetime
from flask import Flask
from flask_cqlalchemy import CQLAlchemy
from flask import request,jsonify
from flask_cassandra import CassandraCluster
from cassandra.query import tuple_factory



app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "playersessionservicekey"
app.config['CASSANDRA_NODES'] = ['127.0.0.1'] 
db = CQLAlchemy(app)
cassandra = CassandraCluster()

# 
# """Creating a class Playersessionservicetable for """
# 

class Playersessionservicetable(db.Model):
    country=db.columns.Text(required=False)
    event=db.columns.Text(required=True)
    player_id=db.columns.Text(required=True,primary_key=True)
    session_id=db.columns.Text(required=True,primary_key=True)
    ts=db.columns.DateTime(required=True,primary_key=True)

# 
#  A function to convert the cassandra resultset to dictionary
# 
def return_dict(result_set):

    temp_list1=[]
    temp_list2=[]
    x=0
    for value in result_set:
        temp_list1.append(value[0])
        temp_list2.append(str('session_id'+"_"+str(x)))
        x=x+1

    dictionary_1=dict(zip(temp_list1,temp_list2))
    return(dictionary_1)

# 
#  A function to check if data is older than one year
# 
def check_older_data(api_date):
    api_date=api_date.date()
    today_date=datetime.date(datetime.now())
    total_days=today_date-api_date

    if total_days.days<=360:
        return(True)
    else:
        return(False)



# 
#  API for receiving event batches (1-10 events / batch)
# 
@app.route('/receiving', methods = ['GET','POST'])
def receiving():
    
    content = request.get_json()
    if 'country' not in content.keys():
         content['country']=None
    else:
        pass

    temp_ts=datetime.strptime(content['ts'], '%Y-%m-%dT%H:%M:%S.%f')
    check_date=check_older_data(temp_ts)


    if check_date==True:
        playersessionservicetable=Playersessionservicetable.create(event=content['event'],country=content['country'],player_id= content['player_id'],session_id=content['session_id'],ts=temp_ts)
        db.sync_db()
        return jsonify(content)
    else:
        print("Data Rejected")
        return jsonify(content)

# 
#  API for fetching last 20 complete sessions for a given player
# 

@app.route('/twenty_complete_sessions', methods = ['GET','POST'])
def twenty_complete_sessions():
    
    content=request.get_json()
    player_id=content['player_id']
   
    
    session = cassandra.connect()
    session.row_factory = tuple_factory
    session.execute("use playersessionservicekey")
    
    row = session.prepare("select session_id from Playersessionservicetable where player_id=? and event='end' limit 20 ALLOW FILTERING")
    bound_statement = row.bind([player_id])
    result_set = session.execute(bound_statement)

    result_set_dict=return_dict(result_set)
    return jsonify(result_set_dict)



if __name__=='__main__':
    app.run(debug=True)