#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Explore: What team commits the most fouls?
#Visualize: Plot the percentage of games that ended in a draw over time.
#Analyze: Does the number of red cards a team receives have an effect on its probability of winning a game?
import pandas as pd
import numpy as np
import seaborn as sns
df=pd.read_csv('H:\Soccer.csv')
df.head()


# In[6]:


"""
Data Dictionary
Column	Explanation
Div	Division the game was played in
Date	The date the game was played
HomeTeam	The home team
AwayTeam	The away team
FTHG	Full time home goals
FTAG	Full time away goals
FTR	Full time result
HTHG	Half time home goals
HTAG	Half time away goals
HTR	Half time result
Referee	The referee of the game
HS	Number of shots taken by home team
AS	Number of shots taken by away team
HST	Number of shots taken by home team on target
AST	Number of shots taken by away team on target
HF	Number of fouls made by home team
AF	Number of fouls made by away team
HC	Number of corners taken by home team
AC	Number of corners taken by away team
HY	Number of yellow cards received by home team
AY	Number of yellow cards received by away team
HR	Number of red cards received by home team
AR	Number of red cards received by away team
"""


# In[4]:


df.shape


# In[5]:


df.describe


# In[14]:


unique_home_Team=df['HomeTeam'].unique()
print(unique_home_Team)


# In[19]:


#Explore: What team commits the most fouls (Home Team)?
import matplotlib.pyplot as plt
sum_HF = df.groupby('HomeTeam')['HF'].sum()
plt.figure(figsize=(15, 6))
plt.bar(sum_HF.index,sum_HF,color='maroon',width=0.4)
plt.xlabel('Home Team')
plt.ylabel('No of Fouls by Home Team)')
plt.title('Home Team Foul Bar Chart')
plt.xticks(rotation=90)
for i,value in enumerate(sum_HF):
    plt.text(i,value,str(value),ha='center',va='bottom')
plt.show()


# In[21]:


#Explore: What team commits the most fouls (Away Team)?
import matplotlib.pyplot as plt
sum_HF = df.groupby('AwayTeam')['AF'].sum()
plt.figure(figsize=(15, 6))
plt.bar(sum_HF.index,sum_HF,color='maroon',width=0.4)
plt.xlabel('Away Team')
plt.ylabel('No of Fouls by Away Team)')
plt.title('Away Team Foul Bar Chart')
plt.xticks(rotation=90)
for i,value in enumerate(sum_HF):
    plt.text(i,value,str(value),ha='center',va='bottom')
plt.show()


# In[24]:


#Visualize: Plot the percentage of games that ended in a draw over time.
selected_columns=df[['Date','FTR']]
print(selected_columns)


# In[28]:


Unique_FTR=df['FTR'].unique
print(Unique_FTR)


# In[31]:


Draw=(df['FTR']=='D').mean()*100
print(Draw)


# In[49]:


plt.figure(figsize=(20, 6))
draw_percentage = (df['FTR'] == 'D').groupby(df['Date']).mean() * 100
plt.plot(draw_percentage.index,draw_percentage,marker='o')
plt.xlabel('Date')
plt.ylabel('Draw Percentage)')
plt.title('Percentage of Draw over Time')
#plt.xticks(rotation=90)
#for i, value in enumerate(draw_percentage):
#    plt.text(i, value, f'{value:.2f}%', ha='center', va='bottom')
for date, percentage in zip(draw_percentage.index, draw_percentage):
    plt.text(date, percentage, f'{percentage:.2f}%', ha='center', va='bottom')

plt.show()


# In[51]:


#Analyze: Does the number of red cards a team receives have an effect on its probability of winning a game?
selected_columns1=df[['HR','FTR']]
print(selected_columns1)


# In[55]:


sum_Away_Team_Win = df[df['FTR']=='A'].groupby('AwayTeam').size()
print (sum_Away_Team_Win )


# In[58]:


Win_percentage = (df['FTR'] == 'A').groupby(df['AwayTeam']).mean() * 100
print(Win_percentage)


# In[60]:


# Calculate the total number of games for each combination of red cards and home team wins
red_card_stats = df.groupby(['HR', 'FTR']).size().unstack(fill_value=0)
print(red_card_stats)
# Calculate the percentage of home team wins for each number of red cards
red_card_stats['Percentage_Home_Win'] = (red_card_stats['H'] / (red_card_stats['H'] + red_card_stats['A'])) * 100

# Display the resulting DataFrame
print(red_card_stats)


# In[ ]:




