import requests

def request_get(url):
    print("Sending request to ", url)
    response = requests.get(url)                                #connects and pings the url in its given parameter and return the status code                    
    print("Requst code recieved is", response.status_code)      #for unit tests as we need to check if the website is up,(200-299 is fine but I just used 200)
    return response.status_code
