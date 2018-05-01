import pandas as pd
import numpy as np
import matplotlib as plt

ad_clicks = pd.read_csv('ad_clicks.csv')
maxUtm = ad_clicks.groupby('utm_source').count().reset_index()
#print(maxUtm)
#is_click = lambda x: True if x != None else False
ad_clicks['is_click'] = ad_clicks["ad_click_timestamp"].isnull()
#ad_clicks['ad_click_timestamp'].apply(is_click)
#print(ad_clicks.head(5))
switch_s = lambda x: True if x == False else False
ad_clicks['is_click'] = ad_clicks['is_click'].apply(switch_s)
#print(ad_clicks.head(5))

clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()
#print(clicks_by_source)
clicks_pivot = clicks_by_source.pivot(columns = "is_click", index = "utm_source", values = "user_id").reset_index()
print(clicks_pivot)
clicks_pivot["percent_clicked"] = (clicks_pivot[True]) / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)
exp_count = ad_clicks.groupby("experimental_group").user_id.count().reset_index()
#print(exp_count) #
print("\n Yes, 827 each. Therefore it is equal")
exp_count_click = ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index()
expCountClickPivot = exp_count_click.pivot(columns = "is_click", index = "experimental_group", values = "user_id")
expCountClickPivot["percTrue"] = expCountClickPivot[True] / (expCountClickPivot[True] + expCountClickPivot[False])
expCountClickPivot.reset_index()
print("\n")
print(expCountClickPivot)
print("\n Users are 7% more likely to click on an add if they are in group A")

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
print(a_clicks.head(5))
print(b_clicks.head(5))

a_clicks_group = a_clicks.groupby(["is_click", "day"]).user_id.count().reset_index().pivot(columns="is_click",index="day", values="user_id")
b_clicks_group = b_clicks.groupby(["is_click", "day"]).user_id.count().reset_index().pivot(columns="is_click",index="day", values="user_id")
a_clicks_group["percentTrueDay"] = a_clicks_group[True] / (a_clicks_group[True] + a_clicks_group[False])
b_clicks_group["percentTrueDay"] = b_clicks_group[True] / (b_clicks_group[True] + b_clicks_group[False])
print("\n People are more likely to click on an A ad on Thursday")
print(a_clicks_group.head(10))
print("\n People are more likely to click on an B ad on Tuesday")
print(b_clicks_group)

print("\nBased on the information given, users are more likely to click on an ad in Group A than in Group B. Users respond more throughout the week with ad A")
