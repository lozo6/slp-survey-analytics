from dotenv import load_dotenv
from dotenv import dotenv_values
import requests

# https://api.qualtrics.com/9d0928392673d-get-survey



load_dotenv()

config = dotenv_values(".env")

datacenterId = config["QUALTRICS_DATA_CENTER_ID"]
apiToken = config["QUALTRICS_API_TOKEN"]
testSurveyId = config["QUALTRICS_SURVEY_ID"]

# https://subdomain.qualtrics.com/API/v3/:collection


url_FullSurvey = 'https://' + datacenterId + '.qualtrics.com/API/v3/survey-definitions/' + testSurveyId 
urlMetaData_surveydetails = url_FullSurvey + '/metadata'

header = {"Content-Type": "application/json", 'X-API-TOKEN': apiToken}

#### get assessment details
details = requests.get(urlMetaData_surveydetails, headers=header)
details_json = details.json()
details_json.keys()
details_json['result'].keys()



#### get survey questions  responses
request = requests.get(url_FullSurvey, headers=header)
request_json = request.json()
list(request_json.keys())

test = request_json['result']
test.keys()
test_questions = test['Questions']
test_questions.keys()
test_questions['QID50'].keys()

for key in test_questions.keys():
    print(test_questions[key]['QuestionText'])
    print(test_questions[key]['QuestionType'])

