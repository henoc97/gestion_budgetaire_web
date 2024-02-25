import requests

class MyEndpoints:
    def __init__(self):
        self.host = "http://127.0.0.1:8000"

    def get_client_budgets(self, client_id):  
        url = f"{self.host}/client/budgets"  
        params = {"client_id": client_id}
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
