# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 23:44:54 2022

@author: natem
"""



import io   
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
import selenium
import matplotlib.pyplot as plt

years=['2009-12-16','2012-01-18','2013-01-17','2014-12-18','2017-01-12','2019-04-04','2021-12-23']
mlinks=["".join (['https://www.transfermarkt.us/statistik/weltrangliste/statistik/stat/datum/',str(hh)]) for hh in years]
#this section of the transfermarkt code will be iterated across all different years
ttt=[i for i in range(len(rank),2)]
#loop that produces link to all pages
#iterating through different year Rankings
all_years=[]
#loops through links for all years in which AFCON took place
for mlink in mlinks:
 url=['','','','','','','','','']
#iterating through each 9 pages of the selected year
 for i in range (0,9):
     url[i]=mlink + '/plus/0/galerie/0/page/' + (str(i+1))
  #loop that goes through all of our pages
 rank=[]
 for link in url:
   headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
   pageTree = requests.get(link, headers=headers)
   #parses the collecte========d html data
   pageSoup = BeautifulSoup(pageTree.text, 'html.parser')
   
 #extracting the different columns 
   ranks=pageSoup.find_all("td",{"class":"hauptlink"})
   for i in ranks:
      z=i.text
      rank.append(z)
    
#Once every page output is appending to a rank output
#each rank should be made part of the fifa rank database and appended to all years
#turn this raw table data into ordered database
#Creating our data frame by adding list columns
      
 tt=[rank[i] for i in range(0,len(rank),2)]
 points=[rank[i] for i in range(1,len(rank),2)]  
 ll=[i for i in range(1,((len(rank)//2)+1))]
 #fifarank=pd.DataFrame()
 fifarank=pd.DataFrame({'Team':tt,'Ranking':ll,'Points':points})   
 all_years.append(fifarank)


#scraping grouo tables from wikpedia
#google/youtbe how to efficiently scrape wikitables
links=['https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations','https://en.wikipedia.org/wiki/2012_Africa_Cup_of_Nations','https://en.wikipedia.org/wiki/2013_Africa_Cup_of_Nations','https://en.wikipedia.org/wiki/2015_Africa_Cup_of_Nations','https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations','https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations','https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations']


#design: for link in links : read all of the links 
#current solution, create list that will be appended for every season 
#list containing links is seperated on the year that the tournament took place
for mlink in mlinks:
 total=[]   
 for link in links:
    headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    pageTree = requests.get(link, headers=headers)
    #parses the collected html data
    pageSoup = BeautifulSoup(pageTree.text, 'html.parser')
    tables=pageSoup.find_all("table",{"class":"wikitable"})

    #reads all the wiki tables as dataframes
    fin=pd.read_html(str(tables))

#filters this table to only include certain length tables(to get the standings tables)
    Groups=[]
    for i in fin:
        if i.shape==(4, 11) or i.shape==(4,9):
            i = i.rename(columns={'Team.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:"[ "}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:" ]"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}vte':'Team'})
            i = i.rename(columns={'Teamvte':'Team'})
            Groups.append(i)
    total.append(Groups)
    
    
#NEXT: ADD RANK TO EACH TEAM
for tour in total:
    for group in tour:
       group['Ranking']=0


        

        
#Ranking of years is kept in all_years, with all_years[0] corresponding to year[0] and so forth
#remove noise and standardize the names of some teams
for yr in range(len(total)):
    for grp in range(len(total[yr])):
        for tm in range(len(total[yr][grp])):        
         total[yr][grp]['Team'][tm]=total[yr][grp]['Team'][tm].replace("(A)","")
         total[yr][grp]['Team'][tm]=total[yr][grp]['Team'][tm].replace("(H)","")
         total[yr][grp]['Team'][tm]=total[yr][grp]['Team'][tm].replace("(D)","")
         total[yr][grp]['Team'][tm]=total[yr][grp]['Team'][tm].replace("Gambia","The Gambia")
         total[yr][grp]['Team'][tm]=total[yr][grp]['Team'][tm].replace("Equatorial Guinea","Equat. Guinea")

# Made an ordered list of lists with the FIFA rankings and then index them similarly
#stripped whitespace of both strings in if statement
for yr in range(len(total)):
    for tourn in range(len(all_years)):
    #making sure that the ranking and AFCON years are the same
     if yr==tourn:
      for grp in range(len(total[yr])):
        for tm in range(len(total[yr][grp])):
           for jjj in range(len(all_years[tourn])):
              if str(all_years[tourn]['Team'][jjj]).strip()==total[yr][grp]['Team'][tm].strip() :
                 # print(int(all_years[tourn]['Ranking'][jjj]))
                  total[yr][grp]['Ranking'][tm]=int(all_years[tourn]['Ranking'][jjj]) 
    

#average functions
#for each group
#sort each group by their fifa rankings to look at pot 3 and pot 4 teams
trn_dif=[]
avg_ran=[]
for tourn in total:
    aa=[]
    bb=[]
    trn_cnt+=1
    grp_cnt=0
    for group in tourn:
        group=group.sort_values(by=['Ranking'],ignore_index=True)
        #reset index after this
        grp_cnt+=1
        avg_rank=np.mean(group['Ranking'])
        bb.append(avg_rank)
        print("The Average of rank group"+ str(grp_cnt)+ ' ' + 'for tournament' + str(trn_cnt) + ' ' + str(avg_rank))

#do this for third minus 4th rank             
    #for pos in range(len(group)):
        rank_dif=group['Ranking'][3]-group['Ranking'][2]
        aa.append(rank_dif)
        rank_dif=str(rank_dif)
        print("The Average of rank difference"+ str(grp_cnt)+ ' ' + 'for tournament' + str(trn_cnt) + ' ' + rank_dif)
       
   #GET AVG difference between third and 4th FOR EACH TOURNAMENT
    trn_dif.append(aa)  
    avg_ran.append(bb)        
#find avg d/nce for each year:
all_time=0
for tr in trn_dif:
    all_time+=np.mean(tr)
    print(np.mean(tr))

#find for entire tournaments
print(np.mean(trn_dif))


#1- sample t-test 
#from scipy.stats import ttest_1samp
##dif_fin=sum(trn_dif,[])
#dif_mean = (np.mean(dif_fin))
#print(dif_mean)
#tset, pval = ttest_1samp(dif_fin, dif_mean)
#print('pvalues', pval)
#if pval < 0.05:    # alpha value is 0.05 or 5%
#   print(" we are rejecting null hypothesis")
#else:
#  print("we are accepting null hypothesis")
  
  
  



#GRAPHING SECTION
G2021=['A','B','C','D','E','F']

#bar plot for the average ranking for each group in 2021 AFCON
  
plt.bar(G2021,avg_ran[6])
plt.title('Avg Fifa Rank of each AFCON 2021 Group')
plt.xlabel('Group')
plt.ylabel('Average Rank of each group')
plt.show()  




 #Graph d/nce between 3rd and 4th pot in each group for 2021
  
plt.bar(G2021,trn_dif[6])
plt.title('Fifa Ranking differences between third and fourth pot teams')
plt.xlabel('Group')
plt.ylabel('Difference in Fifa Rankings(Pot 4- Pot 3)')
plt.show()