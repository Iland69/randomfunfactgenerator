import json
import requests
import win10toast
import time


def get_random_fun_fact():
    """
    This function will return a random fun fact from the API.
    """
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["text"]


def main():
    toast = win10toast.ToastNotifier()
    if toast.show_toast("Fun Fact", get_random_fun_fact(), duration=20, threaded=True):
        time.sleep(300)
        print("Toast was shown")


if __name__ == "__main__":
    while True: main()
