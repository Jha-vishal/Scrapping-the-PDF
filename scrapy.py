#import the library used to query a website
#import urllib2 #if you are using python3+ version,
import urllib.request

#specify the url
OLX = "http://bizjagat.com/state/uttar-pradesh/ghaziabad"
#Query the website and return the html to the variable 'page'
#page = urllib2.urlopen(wiki) #For python 3 use
page = urllib.request.urlopen(OLX)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)
print(soup.prettify())
soup.title
#print(soup.title)
soup.title.string
#print(soup.title.string)

soup.a
#print(soup.a)

soup.find_all("a")
#print(soup.find_all("a"))

all_tables=soup.find_all('table')
#print(all_tables)

for link in all_tables:
    print(link.get("href"))


table=soup.find('div id="add_title"> <span></span><b1> India')
print(table)



#Generate lists
A=["add_title"] #<div> id =
B=["dec"]
C=["Business Type:" ]
D=["Address :"]
E=["Phone : "]  #<div> <b>


for row in right_table.findAll("tr"):
    cells = row.findAll('')
    states= row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))



#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
