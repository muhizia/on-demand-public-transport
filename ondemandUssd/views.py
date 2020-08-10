from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from django.conf import settings
from ondemandUssd.models import Passenger,UssdRideRequest
from ondemandUssd.functions import (checkUserExist,saveSession,
checkUserLevel,saveNewUser,checksessionLevel,
checkPassword,updateSession,userLevel,updateUserPassword,getPassengerDetail,saveRequestLocation)

# view that help us to display the first attempt
@csrf_exempt
def home(request):
    response=""
    
    if request.method =='POST':
        
        sessionId = request.POST.get("sessionId")
        phoneNumber = request.POST.get("phoneNumber")
        text = request.POST.get("text")
        
        textsplit = text.split('*')

        #check if the use already had an account
        if(checkUserExist(phoneNumber) == False) :
     
            if text == "":
                saveSession(sessionId,phoneNumber, 1)
                response = "CON <b>Create Account </b> <br/>"
                response += "Enter 5 values <br/>"
                return HttpResponse (response, content_type="text/plain")

                # if the user created and want to enter his names
            if len(text) == 5 and checksessionLevel(sessionId) == 1:
                updateSession(sessionId,phoneNumber, 2)
                response = "CON Please Enter your Name"
                return HttpResponse (response, content_type="text/plain")

                # After the user enter his names
            elif(len(text) >6) and checksessionLevel(sessionId) == 2 :
                if checkPassword(phoneNumber, textsplit[0]):
                    updateSession(sessionId,phoneNumber, 3)
                    response = "END The user already exist"
                    return HttpResponse (response, content_type="text/plain")
                else:
                    saveNewUser(textsplit[1], phoneNumber, textsplit[0])
                    updateSession(sessionId,phoneNumber, 4)
                    response = "CON Account Created successful <br/>"
                    response += "1. To continue <br>"
                    response += "2. To exit"
                    return HttpResponse (response, content_type="text/plain")
   
            else:
                response = "END Invalid response <br/> during creation"
                return HttpResponse (response, content_type="text/plain")


           

        elif (checkUserExist(phoneNumber) == True):
            if text == "":
                saveSession(sessionId,phoneNumber, 1)
                #textsplit[0] 12345
                response = "CON Welcome to WeGo<br/>"
                response +="Enter your pin<br/>"
                return HttpResponse (response, content_type="text/plain")
            elif checksessionLevel(sessionId) == 1:
                if(checkPassword(phoneNumber, textsplit[0])):
                    updateSession(sessionId,phoneNumber, 2)
                    #textsplit[1] 12345*1
                    response = "CON Book a ride <br/>"
                    response += "1. Request a ride <br/>"
                    response += "2. Change your pin <br/>"
                    return HttpResponse (response, content_type="text/plain")
                else:
                    response ="END Invalid pin <br/>"
                    return HttpResponse (response, content_type="text/plain")
            elif checksessionLevel(sessionId) == 2:

                if textsplit[1] == "1":
                    #textsplit[2] 12345*1*08/03/2020 14:24
                    updateSession(sessionId,phoneNumber, 11)
                    response = "CON Data and Time <br/> "
                    response += "month/day/year hour:minute <br/>"
                    return HttpResponse (response, content_type="text/plain")

                elif textsplit[1] == "2":
                    # textsplit[2] 12345*2*12345
                    updateSession(sessionId,phoneNumber, 3)
                    response = "CON Existing pin <br/>"
                    return HttpResponse (response, content_type="text/plain")
                else:
                    response = "END Invalid response <br/>"
                    return HttpResponse (response, content_type="text/plain")
            elif checksessionLevel(sessionId) == 11:
                  # textsplit[3] 12345*1*08/03/2020 14:24*L12345,L21222*
                updateSession(sessionId,phoneNumber, 12)
                response = "CON picup and dropoff place <br/>"
                response += "Enter the place codes separated by<br/>"
                response += ", Ex: L12345,L21222<br/>"
                return HttpResponse (response, content_type="text/plain")
            elif checksessionLevel(sessionId) == 3:
                    #textsplit[3] 12345*2*12345*54321
                    if checkPassword(phoneNumber,textsplit[0]):
                        updateSession(sessionId,phoneNumber, 12)
                        response = "CON New pin <br/>"
                        return HttpResponse (response, content_type="text/plain")
                    else:
                        response = "END Invalid pin <br/>"
                        return HttpResponse (response, content_type="text/plain")
            elif checksessionLevel(sessionId) == 12 and textsplit[1]=="2":

                    if len(textsplit[3]) == 5:
                        updateUserPassword(phoneNumber, textsplit[3])
                        response = "END Pin updated <br/> <br/>"
                        return HttpResponse (response, content_type="text/plain")
                    else:
                        response = "END invalid pin <br/>"
                        return HttpResponse (response, content_type="text/plain")
            
            elif checksessionLevel(sessionId) == 12 and textsplit[1]=="1":
                updateSession(sessionId,phoneNumber, 13)
                 # textsplit[4] 12345*1*08/03/2020 14:24*L12345,L21222*2
                response = "CON Number of passenger <br/>"
                return HttpResponse (response, content_type="text/plain")
            elif checksessionLevel(sessionId) == 13:
                updateSession(sessionId,phoneNumber, 14)
                # textsplit[5] 12345*1*08/03/2020 14:24*L12345,L21222*2*0
                response = "CON Number of People with disability<br/>"
                return HttpResponse (response, content_type="text/plain")
            elif checksessionLevel(sessionId) == 14:
                passengerDetails = getPassengerDetail(phoneNumber)
                locationsplit = textsplit[3].split(",")
                savedRequest = saveRequestLocation(textsplit[2],locationsplit[0], locationsplit[1],textsplit[4], textsplit[5])
                savedRequest.passengers.add(passengerDetails)
                response = "END payment Detail <br/>"
                response += "Remera Bus Park --><br/>"
                response += "Nyabugogo Bus Park for 450<br/>"
                response += "Rwf<br/>"
                return HttpResponse (response, content_type="text/plain")

                
            if checksessionLevel(sessionId) == 4:
                    # if the user press one to continue and has the passwod *12345*Patrick dushimimanam*1
                if textsplit[2] == "1":
                    updateSession(sessionId,phoneNumber, 5)
                    response = "CON Book a ride <br/>"
                    response += "1. Request a ride <br/>"
                    response += "2. Change your pin <br/>"
                    return HttpResponse (response, content_type="text/plain")
                     # if the user press one to continue and has the passwod *12345*Patrick dushimimanam*2
                elif textsplit[2] == "2" :
                    response = "END Thanks By <br/>" +textsplit[2] 
                    return HttpResponse (response, content_type="text/plain")
                  
            elif checksessionLevel(sessionId) == 5:
                # if the user press one to continue and has the passwod *12345*Patrick dushimimanam*1*1 
                if textsplit[3] == "1":
                    updateSession(sessionId,phoneNumber, 6)
                      # textsplit[4] is pickup time
                    response = "CON Data and Time <br/> "
                    response += "month/day/year hour:minute <br/>"
                    return HttpResponse (response, content_type="text/plain")
                    # if the user press one to continue and has the passwod *12345*Patrick dushimimanam*1*2 
                elif textsplit[3] == "2":
                    updateSession(sessionId,phoneNumber, 6)
                    response = "CON Existing pin <br/>"
                    return HttpResponse (response, content_type="text/plain")
                else:
                    response = "END Invalid response <br/>"
                    return HttpResponse (response, content_type="text/plain")

            
            elif checksessionLevel(sessionId) == 6:
                if textsplit[3] == "2":
                    if checkPassword(phoneNumber,textsplit[4]):
                        updateSession(sessionId,phoneNumber, 7)
                        response = "CON New pin <br/>"
                        return HttpResponse (response, content_type="text/plain")
                    else:
                        response = "END Invalid pin <br/>"
                        return HttpResponse (response, content_type="text/plain")
                    # if the user press one to continue and has the passwod *12345*Patrick dushimimanam*1*1*03/08/2020 21:27
                elif textsplit[3] == "1":
                    #textsplit[5]
                    updateSession(sessionId,phoneNumber, 8)
                    response = "CON pickup and dropoff place <br/>"
                    response += "Enter the place codes separated by<br/>"
                    response += ", Ex: L12345,L21222<br/>"
                    return HttpResponse (response, content_type="text/plain")
                
                
            elif checksessionLevel(sessionId) == 7:
                if len(textsplit[5]) == 5:
                    updateUserPassword(phoneNumber, textsplit[5])
                    response = "END Pin updated <br/> <br/>"
                    return HttpResponse (response, content_type="text/plain")
                else:
                    response = "END invalid pin <br/>"
                    return HttpResponse (response, content_type="text/plain")
            # if the user press one to continue and has the passwod *12345*Patrick dushimimanam*1*1*03/08/2020 21:27*L12345,L21222
            elif checksessionLevel(sessionId) == 8:
                updateSession(sessionId,phoneNumber, 9)
                #textsplit[6]
                response = "CON Number of passenger <br/>"
                return HttpResponse (response, content_type="text/plain")
            elif checksessionLevel(sessionId) == 9:
                updateSession(sessionId,phoneNumber, 10)
                #textsplit[7]
                response = "CON Number of people with disability<br/>"
                return HttpResponse (response, content_type="text/plain")

                # if the user press one to continue and has the passwod *12345*Patrick dushimimanam*1*1*03/08/2020 21:27*L12345,L21222*1
                # if the user press one to continue and has the passwod *12345*Patrick dushimimanam*1*1*03/08/2020 21:27*L12345,L21222*2*3*1
            elif  checksessionLevel(sessionId) == 10:

                passengerDetails = getPassengerDetail(phoneNumber)
                locationsplit = textsplit[5].split(",")
                savedRequest = saveRequestLocation(textsplit[4],locationsplit[0], locationsplit[1],textsplit[6], textsplit[7])
                savedRequest.passengers.add(passengerDetails)

                response = "END Payment Details <br/>"
                response += "Remera Bus Park --><br/>"
                response += "Nyabugogo Bus Park for 450<br/>"
                response += "Rwf<br/>"
                return HttpResponse (response, content_type="text/plain")
                             
        else:

            response = "END Invalid response <br/> "
            return HttpResponse (response, content_type="text/plain")
            






        

                


                    
        