from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def logout(self):
        self.client.get("/v2/user/logout")

    @task
    def login(self):
        self.client.get("/v2/user/login?username=metin&password=123456781")

    @task
    def get_user_info(self):
        self.client.get("/v2/user/metin")

    @task
    def user_create(self):
        payload = {
            "id": 2334455,
            "username": "metin2",
            "firstName": "mete",
            "lastName": "torun",
            "email": "metetorun@gmail.com",
            "password": "56789",
            "phone": "555789988",
            "userStatus": 3
        }
        self.client.post("/v2/user", json=payload)

    @task
    def delete_user(self):
        self.client.delete("/v2/user/metin2")

    @task
    def update_user(self):
        payload2 = {
            "id": 23545546,
            "username": "metin",
            "firstName": "metin",
            "lastName": "yılmaz",
            "email": "testsahibinden2@gmail.com",
            "password": "12345",
            "phone": "5434565676",
            "userStatus": 4
        }
        header_payload={
            "accept":"application/json",
            "Content-Type":"application/json"

        }
        self.client.put("/v2/user/metin23",json=payload2,headers=header_payload)

