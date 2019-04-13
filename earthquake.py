# this is a small project
# we will display all the earthquakes that were recorded a day before and has the magnitude of 2.5 and above
# let's get started
import urllib.request
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
    EqJSON = json.loads(data)
    if "title" in EqJSON["metadata"]:
        print("\n----------------------------------------")
        print(EqJSON["metadata"]["title"])
        print(EqJSON["metadata"]["count"], " events recorded.")
        print("----------------------------------------\n")

    
    # for each event the place where it was recorded and the magnitude
    print("Magnitude --------- Place\n")
    for i in EqJSON["features"]:
        print(i["properties"]["mag"], "------", i["properties"]["place"])
    
    print("----------------------------------------\n")


    # events that only had a magnitude of 4 or above
    print("Magnitude --------- Place\n")
    for i in EqJSON["features"]:
        if i["properties"]["mag"] >= 4:
            print("%2.1f" %i["properties"]["mag"],"------", i["properties"]["place"])
    
    print("----------------------------------------\n")

    
    # events where atleast 1 person reported feeling something
    for i in EqJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print("%2.1f" %i["properties"]["mag"], i["properties"]["place"], " Reported ", feltReports, " times.")

    print("----------------------------------------\n")
    




def main():
    # the main function to collect data from USGS official website
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Now let's open the url and read data inside it
    WebUrl = urllib.request.urlopen(url)
    if(WebUrl.getcode() == 200):
        data = WebUrl.read()
        printResults(data)
    else:
        print("Received errors, cannot parse results")


if __name__ == "__main__":
    main()