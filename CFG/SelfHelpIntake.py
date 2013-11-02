from django.db import models

'''
#Probably be replaced with userObject? 
class Applicant(models.Model):
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    middleInitial = models.CharField(max_length=50)
    ssn = models.CharField(max_length=11)
	dob = models.CharField(max_length= 10)
	prevAddress = models.CharField(max_length= 
'''

class SelfHelpApplication(models.Model):
	dateRecieved = models.CharField(max_length=11)

	#Remainder of information for Applicant
	appPrevAddress = models.CharField(max_length=100)
	appPrevCity = models.CharField(max_length=20)
	appPrevZip = models.CharField(max_length=5)
	appEmployerName = models.CharField(max_length=50)
	appEmployerAddress = models.CharField(max_length=100)
	appEmployerprevCity = models.CharField(max_length=20)
	appEmployerprevZip = models.CharField(max_length=5)
	appYearsThere = models.CharField(max_length=2)

	#Remainder of information for Co-applicant
	appPrevAddress = models.CharField(max_length=100)
	appPrevCity = models.CharField(max_length=20)
	appPrevZip = models.CharField(max_length=5)
	appEmployerName = models.CharField(max_length=50)
	appEmployerAddress = models.CharField(max_length=100)
	appEmployerprevCity = models.CharField(max_length=20)
	appEmployerprevZip = models.CharField(max_length=5)
	appYearsThere = models.CharField(max_length=2)
	
	totalHousehold = models.CharField(max_length=2)
	#Answer to the question is the house over crowded?
	crowdedHouse = models.BooleanField()
	numBedrooms = models.CharField(max_length=1)
	#Answer to the question is anyone in house disabled?
	disabilities = models.BooleanField()
	#Answer to the question do you own a home?
	homeOwner = models.BooleanField()
	#Answer to the question is your name on deed?
	deed = models.BooleanField()
	#List of possible areas plus the users area
	area = (("K", "Kent County"), ("S", "Sussex County"))
	currentArea = models.CharField(max_length=1, choices=area)
	referral = models.CharField(max_length=100)
	
