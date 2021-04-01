import pandas as pd
import numpy as np

df = pd.read_csv('F:/Downloads/weight-height.csv')

df
df.describe()
df.columns

HQ1 = df.Height.quantile(0.25) # for Height Column
HQ3 = df.Height.quantile(0.75)

HIQR = HQ3 - HQ1 #Detect outliers using IQR

HL_limit = HQ1 - 1.5*HIQR
HU_limit = HQ3+1.5*HIQR

df[(df.Height < HL_limit) | (df.Height > HU_limit)] #Here are the outliers

df_Hno_outlier = df[(df.Height > HL_limit) & (df.Height < HU_limit)] #Remove outliers


WQ1 = df.Weight.quantile(0.25) # for Weight Column
WQ3 = df.Weight.quantile(0.75)

WIQR = WQ3 - WQ1 #Detect outliers using IQR

WL_limit = WQ1 - 1.5*WIQR
WU_limit = WQ3+1.5*WIQR

df[(df.Weight < WL_limit) | (df.Weight > WU_limit)] #Here are the outliers

df_Wno_outlier = df[(df.Weight < WL_limit) & (df.Weight > WU_limit)] #Remove outliers
