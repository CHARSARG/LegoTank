# importing the requests library
import requests




def Get(URL,PARAMS):

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
    #print(type(r))
    # extracting data in json format
    data = r.json()
    #print(data)
    return data

"""
# extracting latitude, longitude and formatted address
# of the first matching location
print(data)
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
	%(latitude, longitude,formatted_address))
"""

#Get("https://TankController.charsarg.repl.co/commands",{'nm':'TEST'})
