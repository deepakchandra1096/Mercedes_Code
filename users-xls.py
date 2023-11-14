import requests
from openpyxl import Workbook

# API endpoint
api_url = "https://reqres.in/api/users"

response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:

    user_data = response.json()

    # list of users
    users = user_data.get("data", [])

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.append(["User ID", "First Name", "Last Name", "Email"])

    for user in users:
        user_id = user["id"]
        first_name = user["first_name"]
        last_name = user["last_name"]
        email = user["email"]
        worksheet.append([user_id, first_name, last_name, email])

    workbook.save("user_data.xlsx")

    print("User data has been saved to user_data.xlsx.")
else:
    print(f"Failed to retrieve user data. Status code: {response.status_code}")

