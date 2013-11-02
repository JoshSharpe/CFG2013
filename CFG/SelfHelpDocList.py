from django.db import models

class DocCheckList(models.Models):
	#required
	bankStatements = models.BooleanField(default=False)
	payStubs = models.BooleanField(default=False)
	taxForms = models.BooleanField(default=False)
	childSupport = models.BooleanField(default=False)
	moneyOrder = models.BooleanField(default=False)
	picID = models.BooleanField(default=False)
	landlordContact = models.BooleanField(default=False)

	#if applicable
	socialSecurity = models.BooleanField(default=False)
	foodAssistance = models.BooleanField(default=False)
	TANF = models.BooleanField(default=False)
	divorce = models.BooleanField(default=False)
	bankruptcy = models.BooleanField(default=False)
	alimony = models.BooleanField(default=False)
	
