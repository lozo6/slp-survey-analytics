import pandas as pd
import numpy as np

english_survey = pd.read_csv('data/englishSLP.csv')
urdu_survey = pd.read_csv('data/urduSLP.csv')

def enhanceSurvey(survey, language):
    new_survey = survey.drop([0,1])
    drop_col = ['StartDate', 'EndDate', 'Status', 'IPAddress', 'Progress',
        'Duration (in seconds)', 'Finished', 'RecordedDate', 'ResponseId',
        'RecipientLastName', 'RecipientFirstName', 'RecipientEmail',
        'ExternalReference', 'LocationLatitude', 'LocationLongitude',
        'DistributionChannel', 'UserLanguage']
    dropped_survey = new_survey.drop(drop_col, axis=1)

    dropped_survey.replace(to_replace='', value=np.nan, inplace=True)
    dropped_survey.replace(to_replace=' ', value=np.nan, inplace=True)

    ordered_survey = dropped_survey.reset_index()
    ordered_survey = ordered_survey.drop(['index'], axis=1)


    true_survey = ordered_survey.dropna(thresh=46)
    print(true_survey.sample())

    true_survey.to_csv(f'data/new{language}SLP.csv')

enhanceSurvey(english_survey, 'English')
enhanceSurvey(urdu_survey, 'Urdu')

enhanced_english_df = pd.read_csv('data/newEnglishSLP.csv')
enhanced_urdu_df = pd.read_csv('data/newUrduSLP.csv')