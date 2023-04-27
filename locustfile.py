import time
from locust import HttpUser, task, between

#Sample execution: locust --headless --users 10 --spawn-rate 1 -H https://flaskws.azurewebsites.net:443

class WebApp_test(HttpUser):
    @task(1)
    def users(self):
        self.client.post("/predict", json=
        {
        "CHAS":{
          "0":0
           },
        "RM":{
          "0":6.575
           },
        "TAX":{
          "0":296.0
           },
        "PTRATIO":{
          "0":15.3
           },
        "B":{
          "0":396.9
           },
        "LSTAT":{
          "0":4.98
           }
        }
        )