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
import selenium
import matplotlib.pyplot as plt
import scipy
import ipython
import sympy
import nose
import seaborn
import matplotlib as mpl

    


#years to obtain the rankings for AFCON tournaments
years=['2009-12-16','2012-01-18','2013-01-17','2014-12-18','2017-01-12','2019-04-04','2021-12-23']
mlinks=["".join (['https://www.transfermarkt.us/statistik/weltrangliste/statistik/stat/datum/',str(hh)]) for hh in years]

#function that obtain the transfermarkt National team ranking tables for the selected years
def rank_tbl(x=years,y=mlinks):
    #this section of the transfermarkt code will be iterated across all different years
    #ttt=[i for i in range(len(rank),2)]
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
    return(all_years)


all_years=rank_tbl(years,mlinks)


#obtaining the group tables from wikpedia
links=['https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations','https://en.wikipedia.org/wiki/2012_Africa_Cup_of_Nations',
       'https://en.wikipedia.org/wiki/2013_Africa_Cup_of_Nations','https://en.wikipedia.org/wiki/2015_Africa_Cup_of_Nations',
       'https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations','https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations',
       'https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations']


#design: for link in links : read all of the links 
#current solution, create list that will be appended for every season 
#list containing links is seperated on the year that the tournament took place
def AFCON_Tables(r=0):
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
                i= i.rename(columns={'Team.mw-parser-output .hlist dl,.mw-parser-output .hlist ol,.mw-parser-output .hlist ul{margin:0;padding:0}.mw-parser-output .hlist dd,.mw-parser-output .hlist dt,.mw-parser-output .hlist li{margin:0;display:inline}.mw-parser-output .hlist.inline,.mw-parser-output .hlist.inline dl,.mw-parser-output .hlist.inline ol,.mw-parser-output .hlist.inline ul,.mw-parser-output .hlist dl dl,.mw-parser-output .hlist dl ol,.mw-parser-output .hlist dl ul,.mw-parser-output .hlist ol dl,.mw-parser-output .hlist ol ol,.mw-parser-output .hlist ol ul,.mw-parser-output .hlist ul dl,.mw-parser-output .hlist ul ol,.mw-parser-output .hlist ul ul{display:inline}.mw-parser-output .hlist .mw-empty-li{display:none}.mw-parser-output .hlist dt::after{content:": "}.mw-parser-output .hlist dd::after,.mw-parser-output .hlist li::after{content:" · ";font-weight:bold}.mw-parser-output .hlist dd:last-child::after,.mw-parser-output .hlist dt:last-child::after,.mw-parser-output .hlist li:last-child::after{content:none}.mw-parser-output .hlist dd dd:first-child::before,.mw-parser-output .hlist dd dt:first-child::before,.mw-parser-output .hlist dd li:first-child::before,.mw-parser-output .hlist dt dd:first-child::before,.mw-parser-output .hlist dt dt:first-child::before,.mw-parser-output .hlist dt li:first-child::before,.mw-parser-output .hlist li dd:first-child::before,.mw-parser-output .hlist li dt:first-child::before,.mw-parser-output .hlist li li:first-child::before{content:" (";font-weight:normal}.mw-parser-output .hlist dd dd:last-child::after,.mw-parser-output .hlist dd dt:last-child::after,.mw-parser-output .hlist dd li:last-child::after,.mw-parser-output .hlist dt dd:last-child::after,.mw-parser-output .hlist dt dt:last-child::after,.mw-parser-output .hlist dt li:last-child::after,.mw-parser-output .hlist li dd:last-child::after,.mw-parser-output .hlist li dt:last-child::after,.mw-parser-output .hlist li li:last-child::after{content:")";font-weight:normal}.mw-parser-output .hlist ol{counter-reset:listitem}.mw-parser-output .hlist ol>li{counter-increment:listitem}.mw-parser-output .hlist ol>li::before{content:" "counter(listitem)"\\a0 "}.mw-parser-output .hlist dd ol>li:first-child::before,.mw-parser-output .hlist dt ol>li:first-child::before,.mw-parser-output .hlist li ol>li:first-child::before{content:" ("counter(listitem)"\\a0 "}.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:"[ "}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:" ]"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}vte':'Team'})
                i = i.rename(columns={'Teamvte':'Team'})
                Groups.append(i)
        total.append(Groups)
    return(total)

lll=AFCON_Tables()


#NEXT: initializing the RANK for EACH TEAM
def zero(x):
 for tour in lll:
    for group in tour:
       group['Ranking']=0
 return(lll)  

total=zero(lll)

for yr in range(len(total)):
       for grp in range(len(total[yr])):
                print(total[yr][grp].columns.values.tolist())

#Function that takes a list of dataframes as input and normalizes team name for each AFCON Team
# Before adding a new column with their FIFA world ranking from our obtained from all_years function
def add_rank(gg):
 for yr in range(len(total)):
    for tourn in range(len(all_years)):
    #making sure that the ranking and AFCON years are the same
      if yr==tourn:
       for grp in range(len(total[yr])):
        for tm in range(len(total[yr][grp])):
         total[yr][grp]['Team'][tm]=total[yr][grp]['Team'][tm].replace("(A)","")
         total[yr][grp]['Team'][tm]=total[yr][grp]['Team'][tm].replace("(H)","")
         total[yr][grp]['Team'][tm]=total[yr][grp]['Team'][tm].replace("(D)","")
         total[yr][grp]['Team'][tm]=total[yr][grp]['Team'][tm].replace("Gambia","The Gambia")
         total[yr][grp]['Team'][tm]=total[yr][grp]['Team'][tm].replace("Equatorial Guinea","Equat. Guinea")
         for jjj in range(len(all_years[tourn])):
          if str(all_years[tourn]['Team'][jjj]).strip()==total[yr][grp]['Team'][tm].strip() :
            # print(int(all_years[tourn]['Ranking'][jjj]))
            total[yr][grp]['Ranking'][tm]=int(all_years[tourn]['Ranking'][jjj]) 
 return(total) 

total=add_rank(zero(lll))



#average functions
#for each group
#sort each group by their fifa rankings to look at pot 3 and pot 4 teams

def rank_dif (total,all_years):
 trn_dif=[]
 avg_ran=[]
 for trn_cnt,tourn in enumerate(total):
    aa=[]
    bb=[]
    for grp_cnt,group in enumerate(tourn):
        group=group.sort_values(by=['Ranking'],ignore_index=True)
        #reset index after this
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
 
 return (trn_dif,avg_ran)


trn_dif,avg_ran=rank_dif (total,all_years)
kkk=rank_dif (total,all_years)

#find avg d/nce for each year:
all_time=0
for tr in trn_dif:
    all_time+=np.mean(tr)
    print(np.mean(tr))

#find for entire tournaments
print(np.mean(trn_dif))


##################################GRAPHING SECTION
####################################

#group names 
G2021=['A','B','C','D','E','F']


#create new df for Graphing purposes
df = pd.DataFrame({'Group':G2021, 'Average Strength':avg_ran[6]})


def AFCON_Bar_Plot(dataframe,font, labelcolor, figurecolor,title,xlabel):
    #First, sort data for plotting to create a descending bar chart:          
    dataframe.sort_values(by='Average Strength', inplace=True, ascending=True)
    
    #setting up the variables for graphing
    # Variables
    index = dataframe['Group'] 
    values = dataframe['Average Strength']
    plot_title =title #'Average Fifa Rank of Each AFCON 2021 Group'
    title_size = 20
    font= {'family':font}
    x_label = xlabel#'Average Rank of Each Group'
    y_label='Group'
    
    #Drawing the figure for the plot (viridis color)
    fig, ax = plt.subplots(figsize=(10,6), facecolor = figurecolor)
    mpl.pyplot.viridis()
    
    
    #creating and formating the horizontal bar chart
    bar = ax.barh(index, values)
    plt.tight_layout()
    ax.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
        
    
    
    #setting the title of the graph        
    title = plt.title(plot_title, pad=10, fontdict=font,fontsize=title_size, color=labelcolor)
    title.set_position([.50, 1])
    plt.subplots_adjust(top=0.9, bottom=0.1)
    
    
    
    #formatting the appearance of the barchart
    ax.grid(zorder=0)
    def gradientbars(bars):
        grad = np.atleast_2d(np.linspace(0,1,256))
        ax = bars[0].axes
        lim = ax.get_xlim()+ax.get_ylim()
        for bar in bars:
            bar.set_zorder(1)
            bar.set_facecolor('none')
            x,y = bar.get_xy()
            w, h = bar.get_width(), bar.get_height()
            ax.imshow(grad, extent=[x+w, x, y, y+h], aspect='auto', zorder=1)
        ax.axis(lim)
    gradientbars(bar)
    
    
    rects = ax.patches
    # Place a label for each bar
    for rect in rects:
        # Get X and Y placement of label from rect
        x_value = rect.get_width()
        y_value = rect.get_y() + rect.get_height() / 2
    
        # Number of points between bar and label; change to your liking
        space = -30
        # Vertical alignment for positive values
        ha = 'left'
    
        # If value of bar is negative: place label to the left of the bar
        if x_value < 0:
            # Invert space to place label to the left
            space *= -1
            # Horizontally align label to the right
            ha = 'right'
    
        # Use X value as label and format number
        label = '{:,.0f}'.format(x_value)
    
        # Create annotation
        plt.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at bar end
            xytext=(space, 0),          # Horizontally shift label by `space`
            textcoords='offset points', # Interpret `xytext` as offset in points
            va='center',                # Vertically center label
            ha=ha,                      # Horizontally align label differently for positive and negative values
            color = 'white')            # Change label color to white
        
    
    #hidding the Gridlines
    plt.grid(False)
    
    #Setting the Background color of the plot
    # Background color
    ax.set_facecolor(figurecolor)
    
    
    #Setting the x and y labels
    ax.set_xlabel(x_label, fontsize = 17, fontdict=font, color=labelcolor)
    ax.set_ylabel(y_label, fontsize = 17, fontdict=font, color=labelcolor)

AFCON_Bar_Plot(df,'serif', 'Black', 'Lavender','Average FIFA Rank of Each AFCON 2021 Group','Average Rank of Each Group')

#Creating second dataframe for Analysis of the difference in ranking between third and fourth seeded teams
df2= pd.DataFrame({'Group':G2021, 'Average Strength':trn_dif[6]})


#Utilizing the Barplot function to visualize the difference between 3rd and 4th pot in each group for 2021 AFCON
AFCON_Bar_Plot(df2,'serif', 'Black', 'Lavender','Difference in FIFA Ranking Between Third and Fourth Pot Teams','Difference in Fifa Rank(Pot 4-Pot 3)')
