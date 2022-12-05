# slp-survey-analytics
HHA 502/507 Group Project

## Technologies used
- VSCode
- Python 3.9.4
	- pandas
	- numpy
	- seaborn
	- matplotlib
	- plotly
	- please see all modules used in `requirements.txt`
- Qualtrics


## Exporting data from Qualtrics
- Was able to extract the data with the help of [Professor Hants Williams](https://github.com/hantswilliams/qualtrics_api)
- If you would like to recreate this processor, please clone his repo and `code .env`
- Pieces of information needed:
```yaml
QUALTRICS_DATA_CENTER_ID = "insert here"
QUALTRICS_API_TOKEN = "insert here"
QUALTRICS_SURVEY_ID = "insert here"
```


## Data scripts
- All other scripts were written by [me](https://www.github.com/lozo6), with support from library documentation
- After retrieving data, `script.py` is used to do some light cleaning, `enhance.ipynb` is used to enhance data (with a visualize through Jupyter Notebook), and lastly, `visual.ipynb` is a Jupyter Notebook to see all the visuals required (will change if client changes deliverables)

## /data
Shows all data that was extracted, cleaned, and enhanced


## /images
Shows all charts created with matplotlib.pyplot
