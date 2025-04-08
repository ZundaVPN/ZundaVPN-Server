import requests, json, os
from dotenv import load_dotenv
from modules.hash_encrypt import hash_encrypt

def check_file():
    if not os.path.isfile("register.json"):
        with open("register.json", "w") as f:
            initdata = {}
            initdata["username"] = ""
            initdata["password"] = ""
            json.dump(initdata, f)
            print("insert user information in register.json");exit()
if __name__ == "__main__":
    check_file()
    with open("register.json", "r") as f:
        data = json.load(f)
        try:
            if data["username"] == "" or data["password"] == "": raise KeyError
        except KeyError:
            print("verify register.json failed\ninsert user information again")
            os.remove("register.json")
            check_file()

    username = data["username"]
    password = data["password"]
    encoding_password = hash_encrypt.encoding(password)
    load_dotenv()
    request = {
        "username": username,
        "password": encoding_password,
        "admin": os.getenv("ADMIN_PASSWORD")
    }
    print("data is \n", request)
    request = json.dumps(request)
    headers = {
        "Content-Type": "application/json"
    }
    url = f"http://{os.getenv('HOSTNAME')}:{os.getenv('PORT')}/api/register"
    print(f"target = {url}")
    try:
        response = requests.post(url, data=request, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"register failed\n{e}")
        exit()
    print(f"register success {response.status_code}")
