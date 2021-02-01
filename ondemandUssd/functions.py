from ondemandUssd.models import Passenger,Session_levels,UssdRideRequest

from datetime import datetime

# method for checking if the user exist
def checkUserExist(telephone):
    try:
        getLevel = Passenger.objects.get(telephone=telephone)
    except Passenger.DoesNotExist:
        return False
    else:
        return True

# method for getting passanger based on his phone
def getPassengerDetail(telephone):
    try:
        getPassenger = Passenger.objects.get(telephone=telephone)
    except Passenger.DoesNotExist:
        return False
    else:
        return getPassenger

# method for save the ride details
def saveRequestLocation(pickupTime, departureCity, destinationCity,passengers,disabled):
    
    pickTime = datetime.strptime(pickupTime, "%m/%d/%Y %H:%M")
    savelocation = UssdRideRequest(pickupTime=pickTime,departureCity=departureCity,
    destinationCity=destinationCity,numberOfSeets=passengers,disabledPoeple=disabled)
    savelocation.save()
    return savelocation

# tracking the sessions
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


    

    