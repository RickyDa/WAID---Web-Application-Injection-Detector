class HttpRequest:

    def __init__(self, method="GET", headers={}, body={}, URL=""):
        self.method = method
        self.headers = headers
        self.body = body
        self.URL = URL

    def serialize(self):
        return {
            "method": self.method,
            "URL": self.URL,
            "headers": self.headers,
            "body": self.body,
        }


r = HttpRequest(method="GET", URL="http://www.ynet.co.il")
r_to_json = r.serialize()
print(str(r_to_json).replace("'", '"')
      )  # response = req.post(url='http://127.0.0.1:3000/', json=r_to_json)
# print(response.text)
