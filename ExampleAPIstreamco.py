import json
import requests
import datetime
import keybord
import datetime
import time

def anolus(Atm,Atd,Tom,Tod):
    print('In def functionals Anolus !')
    print(Atm)
    print(Atd)
    print(Tom)
    print(Tod)
    tas = datetime.datetime(2022,Atm,Atd,0,0)
    tas1 = datetime.datetime(2022,Tom,Tod,0,0)
    tass = int(time.mktime(tas.timetuple()))
    tass1=int(time.mktime(tas1.timetuple()))
    API_link_streamko="https://globaldid.streamco.org/api"
    updates=requests.get(API_link_streamko+f"/cdr?_login=TLC_group2_head2&_password=cyK95QZ9&date_from={tass}&date_to={tass1}&with_unanswered=1").json()
    print(updates)
    golf = updates['data']
    return golf
def anolus1(Atm,Atd,Tom,Tod):
    print('In def functionals Anolus1 !')
    print(Atm)
    print(Atd)
    print(Tom)
    print(Tod)
    CountDay=0
    CountDuration=0
    CountAnswerCall=0
    CountNoAnswerCall=0
    tas = datetime.datetime(2022,Atm,Atd,0,0)
    tas1 = datetime.datetime(2022,Tom,Tod,0,0)
    tass = int(time.mktime(tas.timetuple()))
    tass1=int(time.mktime(tas1.timetuple()))
    API_link_streamko="https://globaldid.streamco.org/api"
    updates=requests.get(API_link_streamko+f"/cdr?_login=TLC_group2_head2&_password=cyK95QZ9&date_from={tass}&date_to={tass1}&with_unanswered=1&with_hangupcause=1").json()
    kurkuma = updates['data']
    for i in kurkuma:
        CountDay+=1
        CountDuration+=int(i['duration'])
        print('duration:')
        print(CountDuration)
        print(i['duration'])
        if i['billsec'] == '0':
            CountNoAnswerCall+=1
    API_link_streamko="https://globaldid.streamco.org/api"
    updates=requests.get(API_link_streamko+f"/cdr?_login=TLC_group2_head2&_password=cyK95QZ9&date_from={tass}&date_to={tass1}").json()
    kurkuma=updates['data']
    for i in kurkuma:
        CountAnswerCall+=1
    print(updates)
#    golf = updates['data']
    print('CountAnswer : ' ,CountAnswerCall,'CountDuration : ',CountDuration)
    return [CountAnswerCall,CountNoAnswerCall,CountDuration,CountDay]
tas = datetime.datetime(2022, 4, 1, 0, 0)
tas1 = datetime.datetime(2022, 6, 15, 0, 0)
tass=int(time.mktime(tas.timetuple()))
tass1=int(time.mktime(tas1.timetuple()))
#print(tass)
#print(tass1)
#print(time.mktime(tas.timetuple()))
#print(time.mktime(tas1.timetuple()))
#tas3 = datetime.datetime(tas1-tas)
#print(time.mktime(tas3.timetuple()))
#print(tas-datetime.datetime(1970,1,1).second)
ts = int("1284101485")
ts1 = int("1654653775")
#print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
#print(datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S'))
#print(datetime.date.today().day)
#print(datetime.date.today().month)
#print(datetime.datetime.fromtimestamp(8).strftime('%S'))



#TLC_group2_head2
#cyK95QZ9
API_link_streamko="https://globaldid.streamco.org/api"
updates=requests.get(API_link_streamko+f"/cdr?_login=pashtet&_password=nKk38m8T3R&date_from={tass}&date_to={tass1}&with_unanswered=1&with_hangupcause=1").json()
print(updates)
#print(updates['data'])
#ash=updates['data'
# ]
#print(ash)
#for i in ash:
#    print(i['calldate'],i['dst'],i['hangupcause'])
