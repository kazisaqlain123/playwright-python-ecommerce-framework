import requests


API_BASE_URL = "https://automationexercise.com/api"


def create_account(user: dict[str, str]) -> None:
    payload = {
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
        "title": user["title"],
        "birth_date": user["day"],
        "birth_month": user["month"],
        "birth_year": user["year"],
        "firstname": user["first_name"],
        "lastname": user["last_name"],
        "company": user["company"],
        "address1": user["address"],
        "address2": user["address2"],
        "country": user["country"],
        "zipcode": user["zipcode"],
        "state": user["state"],
        "city": user["city"],
        "mobile_number": user["mobile_number"],
    }

    response = requests.post(
        f"{API_BASE_URL}/createAccount",
        data=payload,
        timeout=30
    )

    response.raise_for_status()

    response_body = response.json()

    assert response_body["responseCode"] == 201, response_body


def delete_account(email: str, password: str) -> None:
    response = requests.delete(
        f"{API_BASE_URL}/deleteAccount",
        data={
            "email": email,
            "password": password
        },
        timeout=30
    )

    response.raise_for_status()

    response_body = response.json()

    assert response_body["responseCode"] == 200, response_body