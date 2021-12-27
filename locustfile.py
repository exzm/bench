import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/api-front/users/is-active-session")
        self.client.get("/api-front/profile-user/contracts")

#     @task(3)
#     def view_items(self):
#         for item_id in range(10):
#             self.client.get(f"/item?id={item_id}", name="/item")
#             time.sleep(1)

    def on_start(self):
        self.client.post("/api-front/users/login", json={"username":"", "password":""})