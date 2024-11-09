#!/usr/bin/env python
# coding: utf-8

# In[1]:


from googleapiclient.discovery import build
import pandas as pd


def get_Custom_Channels_data(youtube, keyword):
    request = youtube.search().list(
        part='snippet',
        maxResults=results,
        q=keyword
    )
    response = request.execute()

    return response


def get_channel_statistics(youtube, li):
    request = youtube.channels().list(
        part='snippet,statistics',
        maxResults=1,
        id=li
    )
    response = request.execute()

    return response

def Collect_info(Channel_Stats):
        for i in range(results):
            Channel_Statistics = [{"Channel_ID": Channel_Stats[i]["items"][0]["id"],
                                   "Channel_name": Channel_Stats[i]["items"][0]["snippet"]["title"],
                                   "Published_Date": Channel_Stats[i]["items"][0]["snippet"]["publishedAt"],
                                   "Views": Channel_Stats[i]["items"][0]["statistics"]["viewCount"],
                                   "subscriberCount": Channel_Stats[i]["items"][0]["statistics"]["subscriberCount"],
                                   "Videos": Channel_Stats[i]["items"][0]["statistics"]["videoCount"],
                                   }
                                  ]
            data_collected.append(Channel_Statistics)
        return (data_collected)


service_name = "youtube"
api_key='Have your Own Key'

youtube=build("youtube","v3",developerKey=api_key)

keyword=["Data Product Dojo"]
results=int(input("Enter the results:"))


# In[2]:


for keyword_counter in range(len(keyword)):
    data=get_Custom_Channels_data(youtube,keyword[keyword_counter])
    li=[]
    for i in range(results):
        new = data['items'][i]['snippet']['channelId']
        li.append(new)

    response_li=[]
    for i in range(results):
        response_li_temp=get_channel_statistics(youtube,li[i])
        response_li.append(response_li_temp)


    data_collected=[]
    Raw_Data=Collect_info(response_li)

    final_li=[]
    for i in range(results):
        temp=Raw_Data[i][0]
        final_li.append(temp)

    df_temp = pd.DataFrame(final_li)
    df_temp["Keyword"]=keyword[keyword_counter]
    df=df_temp.drop_duplicates()
    
    df.to_csv(f'C:\Manikanta\Projects\YT\{keyword[keyword_counter]}.csv',index=False)
    


# In[ ]:




