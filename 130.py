import pandas as pd
import csv
df=pd.read_csv("total_stars.csv")
print(df.columns)
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
print(df.columns)
finaldata=df.dropna()
finaldata.reset_index(drop=True,inplace=True)
finaldata.to_csv("final_data.csv")