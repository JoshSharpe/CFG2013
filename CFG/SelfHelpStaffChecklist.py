from django.db import models

class Procedure(models.Model):
	dateComplete = models.CharField(max_length=11)
	signature = models.BooleanField()

class SelfHelpStaffChecklist(models.Model):
	area = (("K", "Kent County"), ("S", "Sussex County"))
	currentArea = models.CharField(max_length=1, choices=area)
	ami = models.BooleanField()
	
	#Step 1: Orientation
	orientation = models.ForeignKey('Procedure')
	orientationDateComplete = models.CharField(max_length=11)
	orientationDateSignature = models.BooleanField()
	
	#Step 2: Credit Review and Counseling
	creditPlan = models.ForeignKey('Procedure')
	docCheckList = models.ForeignKey('Procedure')
	counselSession = models.ForeignKey('Procedure')
	totalCreditReview = models.ForeignKey('Procedure')
	
	#Step 3: If Credit Ready
	updatePaystubs = models.ForeignKey('Procedure')
	assets = models.ForeignKey('Procedure')
	recentPaystubs = models.ForeignKey('Procedure')
	recentTaxes = models.ForeignKey('Procedure')
	childSupportOrder = models.ForeignKey('Procedure')
	childSupportHistory = models.ForeignKey('Procedure')
	picIDs = models.ForeignKey('Procedure')
	socialSecurityLetter = models.ForeignKey('Procedure')
	monthlyPension = models.ForeignKey('Procedure')
	purchaseOfCare = models.ForeignKey('Procedure')
	foodAssistance = models.ForeignKey('Procedure')
	tanfLetter = models.ForeignKey('Procedure')
	divorce = models.ForeignKey('Procedure')
	bankruptcy = models.ForeignKey('Procedure')
	alimony = models.ForeignKey('Procedure')
	mortgage = models.ForeignKey('Procedure')
	release = models.ForeignKey('Procedure')

	#Step 4: Initial Income Eligibility Determined
	ifIneligible = models.ForeignKey('Procedure')
	ifEligible = models.ForeignKey('Procedure')
	elegibility = models.ForeignKey('Proecdure')

	#Step 5: Complete Loan application and submit to USDA: 
	totalApplication = models.ForeignKey('Procedure')

	#Step 6: Request Cost Estimate
	requestEstimate = models.ForeignKey('Procedure')
	constructionDocumentation = models.ForeignKey('Procedure')
	
	#Step 7: Submit Property information to USDA for Appraisal Request
	usdaAppraisalRequest = models.ForeignKey('Procedure')

	#Step 8: USDA Appraisal
	usdaInterview = models.ForeignKey('Procedure')

	#Step 9: Schedule Loan for Closing with USDA, Client, and Client’s Attorney
	scheduleClosing = models.ForiengKey('Procedure')

	#Step 10: Request Survey
	requestSurvey = models.ForiengKey('Procedure')

	#Step 11: Closing
	requestTitle = models.ForiengKey('Procedure')
	forwardSurvey = models.ForiengKey('Procedure')
	reviewHUD = models.ForiengKey('Procedure')


