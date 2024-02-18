#API Testing
import requests
import random
from selenium import webdriver

#1
# response = requests.get("https://api.github.com/users/avielb/repos")
# actual = len(response.json())
# expected = 5
# assert actual > expected

#2
#to get random name
# def get_random_name():
#     names = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
#     return random.choice(names)
#
# def check_age(name):
#
#     try:
#         response = requests.get(f"https://api.agify.io/?name={name}")
#         data = response.json()
#
#         age = data.get('age')
#         if age is not None:
#             assert 0 <= age <= 120
#             print(f"The age for {name} is {age}, which is within the valid range.")
#         else:
#             print(f"No age information available for {name}.")
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching data from Agify API: {e}")
#
# def main():
#     for _ in range(3):
#         random_name = get_random_name()
#         print(f"Checking age for {random_name}...")
#         check_age(random_name)
#
#
# if __name__ == "__main__":
#     main()


#3
#Testing universities API

# response = requests.get("http://universities.hipolabs.com/search?country=Israel")
# actual = len(response.json())
# expected = 5
# assert actual >= expected
# print("Number of Unis is " + str(actual)) #just for me to check

#4
#test that the title is “YCombinator”
driver = webdriver.Chrome()
driver.get("https://www.ycombinator.com/")
assert driver.title == "Y Combinator"

#5
#title is “Docker HubContainer Image Library | App Containerization”


