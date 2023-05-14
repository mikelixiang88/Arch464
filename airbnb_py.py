# A program to analyze Airbnb listings
# 04-26-2023
# By Mike Li

import pandas as pd

# reading csv file

dataframe=pd.read_csv("listings.csv")

# filter data frame to Los Angeles

dataframe_la=dataframe[dataframe.neighbourhood_group=="City of Los Angeles"]

# Initialize variables
neighbourhood=[]
count=[]
count_p=[]
def lookup(check,num_list,avaliability):
    is_found=False
    for i in range(len(neighbourhood)):
        if neighbourhood[i]==check:
            is_found=True
            count[i]+=1
            if num_list>1 and avaliability>=180:
                count_p[i]+=1
    if is_found==False:
        neighbourhood.append(check)
        count.append(1)
        if num_list>1 and avaliability>=180:
            count_p.append(1)
        else:
            count_p.append(0)

# iterate
for index, row in dataframe_la.iterrows():
    lookup(row['neighbourhood'],row['calculated_host_listings_count'],row['availability_365'])

relative_p=[]
for x in range(len(neighbourhood)):
    relative_p.append(float(count_p[x]/count[x]))

print("______________________________________________________")
relative_p, neighbourhood, count=zip(*sorted(zip(relative_p, neighbourhood, count)))
for z in range(len(neighbourhood)):
    if count[z]<=20:
        print(neighbourhood[z]+": "+str(relative_p[z])+" Count: "+str(count[z]))
