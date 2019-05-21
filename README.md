# 20% Project Semester 2: Utilizing Data Using API's 
### To run: 
Download client libraries (ensure you are using the most recent PIP update!):
```python
pip3 install pytrends
pip3 install google-api-python-client
pip3 install plotly 
```
You will need to create a Plotly account, you can do this at https://plot.ly/python/getting-started/

Use Analysis.py file to create graphs.

Type |  Method | Usage | Inputs
--- |  --- | --- | ---
 Private | __init__() in incident class | Outlines the instance data for event nodes |  date, location, dead, injured, name, results (number of hits)
 Private | convertDate() in incident class | Converts the date into a number for easy comparison | The date as a string
 Private | plotly.tools.set_credentials_file() | input plotly credentials | username and APIkey
 Private | google_search() | initilizes a Google search object using the Python client library to search for number of hits | search term, API key and CSE key (obtained by signing up for Google API account)
 For users | py.iplot() | will create a graph in your plotly accountusing specified data sets | data (Json object), name of graph

When code is running in terminal, will produce an output similar to this: 
![alt text](https://github.com/mmyhill20/APIResearch/blob/master/Code%20Running%20in%20Terminal.png "Code Running in Terminal")
Will produce graphs similar to this: 
![alt text](https://github.com/mmyhill20/APIResearch/blob/master/ExampleGraph.png)

### Future Goals: 

* Having problems maxing out Google search API limits, would like to add all events as nodes to plot

* Make a larger variety of graphs (compare internet usage by age group to time between shootings)
