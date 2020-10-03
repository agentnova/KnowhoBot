import requests
import datetime,pytz
from firebase import firebase
from creds import cred

firebase = firebase.FirebaseApplication(cred.DB_URL)
date=datetime.datetime.utcnow()
date2=date.replace(tzinfo=pytz.UTC)
date=date2.astimezone(pytz.timezone("Asia/Kolkata"))
date=str(date)
date=date[0:10]
today_date = int(date.replace("-", ""))

def check(chatids):
    chatid = chatids
    data = {
        "uname": chatid,
        "count": 0,
        "date": today_date
    }
    result = firebase.get('/users', chatid)
    if result:
        date = result["date"]
        count = result["count"]
        if not date == today_date:
            firebase.put('/users', chatid, data)
            out = "not yet"
        else:
            if count > 5:
                out = "limit reached"
            else:
                count += 1
                data2 = {
                    "uname": chatid,
                    "count": count,
                    "date": today_date
                }
                firebase.put('/users', chatid, data2)
                out = "not yet"
    else:
        firebase.put('/users', chatid, data)
        out = "not yet"
    return out

def truecaller_search(token, num):
    g = "https://account-asia-south1.truecaller.com/v2.1/credentials/check?encoding=json"
    h = {
        "Host": "account-asia-south1.truecaller.com",
        "authorization": token,
        "content-type": "application/json; charset=UTF-8",
        "content-length": "42",
        "accept-encoding": "gzip",
        "user-agent": "Truecaller/11.5.7 (Android;10)"
    }
    requests.post(g, headers=h, timeout=5, data={"reason": "restored_from_account_manager"})

    turl = "https://search5-noneu.truecaller.com/v2/search?q=" + num + "&countryCode=IN&type=4&locAddr=&placement=SEARCHRESULTS%2CHISTORY%2CDETAILS&encoding=json"
    theaders = {
        "user-agent": "Truecaller/11.5.7 (Android;10)",
        "Accept-Encoding": "gzip",
        "authorization": token,
        "Host": "search5-noneu.truecaller.com"
    }
    tresponse = requests.get(turl, headers=theaders, timeout=5)

    return tresponse

def eyecon_search(num):
    url = "https://api.eyecon-app.com/app/getnames.jsp?cli=91" + num + "&lang=en&is_callerid=true&is_ic=true&cv=vc_312_vn_2.0.312_a&requestApi=URLconnection&source=Other"
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; GM1903 Build/QKQ1.190716.003)",
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "e-auth-v": cred.E_AUTH_V,
        "e-auth-c": cred.E_AUTH_C,
        "e-auth": cred.E_AUTH,
        "content-type": "application/x-www-form-urlencoded",
        "Host": "api.eyecon-app.com"
    }
    response = requests.post(url, headers=headers, timeout=5)
    return response

def fb_search(num):
    fburl = "https://api.eyecon-app.com/app/pic?cli=91" + num + "&is_callerid=true&size=big&type=0&cancelfresh=0&cv=vc_312_vn_2.0.312_a"
    fbheaders = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; GM1903 Build/QKQ1.190716.003)",
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "e-auth-v": cred.E_AUTH_V,
        "e-auth-c": cred.E_AUTH_C,
        "e-auth": cred.E_AUTH,
        "Host": "api.eyecon-app.com"
    }
    fbres = requests.get(fburl, headers=fbheaders)
    return fbres

def searches():
    a = firebase.get('/stats', 'total_searches')
    data = {
        "total_searches": a['total_searches'] + 1
    }
    firebase.put('/stats', 'total_searches', data)

def log():
    knowho_users = firebase.get('/users', '')
    searches = firebase.get('/stats', 'total_searches')
    lst1 = []
    act = []
    for k, v in knowho_users.items():
        lst1.append("u")
        if (v['date'] == today_date):
            act.append("d")
    total_search = f"{searches['total_searches']}"
    total_users = f"{lst1.count('u')}"
    active_today = f"{act.count('d')}"

    data={
        "active_users":active_today,
        "total_searches":total_search,
        "total_users":total_users
    }
    firebase.put('/stats',date,data)

def logreturn():
    knowho_users = firebase.get('/users', '')
    searches = firebase.get('/stats', 'total_searches')
    lst1 = []
    act = []
    for k, v in knowho_users.items():
        lst1.append("u")
        if (v['date'] == today_date):
            act.append("d")
    total_search = f"`Total numbers searched` : **{searches['total_searches']}**"
    total_users = f"`Total bot users`                 : **{lst1.count('u')}**"
    active_today = f"`Active users today`          : **{act.count('d')}**"
    stato=f"\n{total_search}\n{total_users}\n{active_today}"
    return stato




