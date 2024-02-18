import requests
import random


def generate_random_name():
    names = ["John", "Alice", "Bob", "Eve", "Charlie", "Olivia", "Daniel", "Emma"]
    return random.choice(names)


def check_age(name):
    agify_api_url = f"https://api.agify.io/?name={name}"

    try:
        response = requests.get(agify_api_url)
        data = response.json()

        assert 'age' in data, f"Unable to retrieve age information for {name}"

        age = data['age']
        assert 0 <= age <= 120, f"The age for {name} is {age}, which is outside the valid range."
        print(f"The age for {name} is {age}, which is within the valid range.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Agify API: {e}")


def main():
    for _ in range(3):
        random_name = generate_random_name()
        print(f"Checking age for {random_name}...")
        check_age(random_name)


if __name__ == "__main__":
    main()
