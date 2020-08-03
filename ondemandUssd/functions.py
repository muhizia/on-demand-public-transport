from ondemandUssd.models import Passenger,Session_levels,RideRequest

from datetime import datetime

def checkUserExist(telephone):
    try:
        getLevel = Passenger.objects.get(telephone=telephone)
    except Passenger.DoesNotExist:
        return False
    else:
        return True
def getPassengerDetail(telephone):
    try:
        getPassenger = Passenger.objects.get(telephone=telephone)
    except Passenger.DoesNotExist:
        return False
    else:
        return getPassenger

def saveRequestLocation(pickupTime, departureCity, destinationCity):
    pickTime = datetime.strptime(pickupTime, "%m/%d/%Y %H:%M")
    savelocation = RideRequest(pickupTime=pickTime,departureCity=departureCity,destinationCity=destinationCity)
    savelocation.save()

def saveSession(session,telephone, level):
    
    getLevel = Session_levels(session_id=session,telephone=telephone, level=level)
    getLevel.save()

def checkUserLevel(telephone):
    try:
        getUserLevel = Passenger.objects.get(telephone=telephone)
    except Passenger.DoesNotExist:
        return 0
    else:
        return getUserLevel.level

def checksessionLevel(session):
    try:   
        getSesssionLevel = Session_levels.objects.get(session_id= session)
    except Session_levels.DoesNotExist:
        return 0
    else:
         return getSesssionLevel.level

def saveNewUser(names, phoneNumber, password):
    global saveNew
    saveNew = Passenger(names=names, telephone=phoneNumber, password=password)
    saveNew.save()

def checkPassword(telephone,password):
        try:
            checkpassword = Passenger.objects.get(telephone=telephone)
        except Passenger.DoesNotExist:
            return False
        else:
            if(checkpassword.password == password):
                return True
            else:
                return False

def updateUserPassword(telephone, password):
    try:
        updatepassword = Passenger.objects.get(telephone=telephone)
    except Passenger.DoesNotExist:
        return False
    else:
        updatepassword.password = password
        updatepassword.save()
        return True

   
def updateSession(sesssion, telephone, level):
    try:      
        updatesession = Session_levels.objects.get(session_id=sesssion)
    except Session_levels.DoesNotExist:
        return 0
    else:
        updatesession.level = level
        updatesession.save()
        return 1
    


def userLevel(telephone):
    try:
        getLevel = Passenger.objects.get(telephone=telephone)
    except Passenger.DoesNotExist:
        return 0
    else:
        
        return getLevel.level


    

    