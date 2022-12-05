import pandas as pd
import numpy as np

df = pd.read_csv('data/englishSLP.csv')

df.info()

print(df.columns)

new_df = df.drop([0,1])
new_df.head(5)

drop_col = ['StartDate', 'EndDate', 'Status', 'IPAddress', 'Progress',
        'Duration (in seconds)', 'Finished', 'RecordedDate', 'ResponseId',
        'RecipientLastName', 'RecipientFirstName', 'RecipientEmail',
        'ExternalReference', 'LocationLatitude', 'LocationLongitude',
        'DistributionChannel', 'UserLanguage']

dropped_df = new_df.drop(drop_col, axis=1)
dropped_df.sample(5)

dropped_df.isnull().sum()

dropped_df.replace(to_replace='', value=np.nan, inplace=True)
dropped_df.replace(to_replace=' ', value=np.nan, inplace=True)

dropped_df.columns

ordered_df = dropped_df.reset_index()
ordered_df = ordered_df.drop(['index'], axis=1)
ordered_df.head(5)

# 44 not nan values
true_df = ordered_df.dropna(thresh=44)

true_df.sample(5)

true_df.to_csv('data/newEnglishSLP.csv')
