from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Time between consecutive tasks

    @task
    def get_person(self):
        endpoint = '/people/1/'
        self.client.get(endpoint)

    @task
    def get_planet(self):
        endpoint = '/planets/42/'
        self.client.get(endpoint)

    @task
    def get_starship(self):
        endpoint = '/starships/100/'
        self.client.get(endpoint)

