import urllib.request
import json

def consume(data):
    body = str.encode(json.dumps(data))
    url = 'https://uswestcentral.services.azureml.net/subscriptions/0a7bdcbe7f3045eaaabec35ccfd09cf9/services/0bb3b56e7072403ba314de9cfe4f719f/execute?api-version=2.0&format=swagger'
    api_key = '4ZE8WkZBOugavQa6TNunJ1TYj9bEOb3CZV5dW8iTs0DgbC8ZStrJ+rYZTwZ7Y+fNN4QtUE9tWVt0CKPj52ryDQ=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        resultRead = response.read()
        resultLoads = json.loads(resultRead)
        return resultLoads

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
        return(error)