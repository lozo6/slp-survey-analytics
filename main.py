import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('data/englishSLP.csv')

df.shape

df.info()

df.columns()
