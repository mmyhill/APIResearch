class incident:
    def __init__(self, date, location, dead, injured, name):
        self.date = self.convertDate(date)
        self.location = location
        self.dead = dead
        self.injured = injured
        self.name = name

    def convertDate(self, dateStr): #converts month to number
        daysIntoYear = int(dateStr[dateStr.find(" ") + 1 : dateStr.find(",")])
        # print("|" + str(daysIntoYear) + "|")
        # print(int(daysIntoYear))
        month = dateStr[1 : dateStr.find(" ")]
        if(month == "February"):
            daysIntoYear += 31
        elif(month == "March"):
            daysIntoYear += 59
        elif(month == "April"):
            daysIntoYear += 90
        elif(month == "May"):
            daysIntoYear += 120
        elif(month == "June"):
            daysIntoYear += 151
        elif(month == "July"):
            daysIntoYear += 181
        elif(month == "August"):
            daysIntoYear += 212
        elif(month == "September"):
            daysIntoYear += 242
        elif(month == "October"):
            daysIntoYear += 273
        elif(month == "November"):
            daysIntoYear += 303
        elif(month == "December"): #cant be else. could just be january
            daysIntoYear += 334
        year = dateStr[dateStr.find(", ") + 2 : len(dateStr)]
        # print(int(year))
        return int(daysIntoYear) + 365 * int(year)


#google trends
from pytrends.request import TrendReq

#google search
from googleapiclient.discovery import build
import pprint

#plotly
import plotly.graph_objs as go
import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='mmyhill20', api_key='jHBPMuT2JRAT0I685b50')

shootings = open("Shootings.txt","r").read()

events = []

#Format of shootings.csv: Date,Location,Dead,Injured,Total,Description

# pytrends = TrendReq(hl='en-US', tz=360)

#trends

# print(search)
# pytrend = TrendReq()

# # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
# pytrend.build_payload(kw_list= ["Las Vegas shooting"])
#
# # Interest Over Time
# interest_over_time_df = pytrend.interest_over_time()
# print(interest_over_time_df.head())
#
# # Interest by Region
# interest_by_region_df = pytrend.interest_by_region()
# print(interest_by_region_df.head())
#
# # Related Queries, returns a dictionary of dataframes
# related_queries_dict = pytrend.related_queries()
# print(related_queries_dict)

#search
my_api_key = "AIzaSyDOsPrEf-IOe1VBGqCK-cXbCPdhTQ8KRsM"
my_cse_id = "013345418863666117125:4xnh0o78sse"

def google_search(search_term, api_key, cse_id): #**kwargs ???
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id).execute()

    return res['searchInformation']['totalResults']

# results = google_search(
#     'stackoverflow', my_api_key, my_cse_id)
# print(results)

count = 0
for event in range(182):#create all nodes of shootings for analysis
    date = shootings[1 : shootings.find('",')]
    # print(date)
    shootings = shootings[shootings.find(',"') + 1 : len(shootings)] #does this automatically go to end?
    # print(shootings)
    location = shootings[shootings.find('\"') + 1 : shootings.find('",')]
    # print(location)
    shootings = shootings[shootings.find('",') + 2 : len(shootings)]
    # shootings = shootings[shootings.find('\"') : len(shootings)]
    dead = shootings[0: shootings.find(',')]
    # print(dead)
    shootings = shootings[shootings.find(',') + 1 : len(shootings)]
    injured = shootings[0 : shootings.find(',')]
    # print(injured)
    shootings = shootings[shootings.find(',') : len(shootings)]
    name = shootings[shootings.find('\"') + 1 : shootings.find(':')]
    print(name)
    shootings = shootings[shootings.find('"\n"') + 1  : len(shootings)] #goes to next event?
    # print(shootings)
    newNode = incident(date, location, dead, injured, name)
    events.append(newNode)

    print(len(events))

# print(len(events))



#graphing/analysis:

# number hits vs. time until next shooting
# x = []
# y = []
# temp = shootings #shallow or deep copy???
# for line in range(shootings.count('\n')):
#     shootingDate = temp[temp.find('\"') + 1 : temp.find(',') - 1]
#     for comma in range(6):
#
#     shootingName =
#
#
# trace1 = go.Scatter(
#     x =
#     y = np.random.randn(500),
#     mode='markers',
#     marker=dict(
#         size=16,
#         color = np.random.randn(500), #set color equal to a variable
#         colorscale='Viridis',
#         showscale=True
#     )
# )
# data = [trace1]
#
# py.iplot(data, filename='scatter-plot-with-colorscale')

if __name__ == '__main__':
  main()
