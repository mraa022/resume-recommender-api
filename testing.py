import requests
import json

url = "https://adnanbadri.pythonanywhere.com/recommend"
data = {
    "resumes": [
    {
        "_id": "65d45805238cc1386cb17efb",
        "jobs": [
            {
                "_id": "65ba23483af837a39e9e17ed",
                "userEmail": "adnanbadri99@gmail.com",
                "jobCategory": "research",
                "jobTitle": "USRA research",
                "companyName": "wilfrid-laurier",
                "startDate": "2024-01-09T00:00:00.000Z",
                "endDate": "2024-04-09T00:00:00.000Z",
                "city": "Kitchener",
                "country": "Canada",
                "jobResponsibilities": [
                    "studied algebra",
                    "studied graph theory",
                    "studied deez nuts"
                ],
                "__v": 0
            }
        ],
        "projects": [
            {
                "_id": "65b9e6441045a22dc75bf254",
                "userEmail": "adnanbadri99@gmail.com",
                "projectCategory": "software-dev",
                "projectTitle": "hello world",
                "projectSubtitle": "python|java|c",
                "projectDescription": [
                    "lol",
                    "lol 2"
                ],
                "__v": 0
            }
        ],
        "education": {
            "_id": "65d429669831c9686f2b3f55",
            "userEmail": "adnanbadri99@gmail.com",
            "degree": "hi",
            "school": "fds",
            "city": "dsaf",
            "country": "f",
            "startDate": "f",
            "endDate": "ee",
            "__v": 0
        }
    },
    {
        "_id": "65d458a0238cc1386cb17f1f",
        "jobs": [
            {
                "_id": "65ba23483af837a39e9e17ed",
                "userEmail": "adnanbadri99@gmail.com",
                "jobCategory": "research",
                "jobTitle": "USRA research",
                "companyName": "wilfrid-laurier",
                "startDate": "2024-01-09T00:00:00.000Z",
                "endDate": "2024-04-09T00:00:00.000Z",
                "city": "Kitchener",
                "country": "Canada",
                "jobResponsibilities": [
                    "studied algebra",
                    "studied graph theory",
                    "studied deez nuts"
                ],
                "__v": 0
            },
            {
                "_id": "65ba22593af837a39e9e17b6",
                "userEmail": "adnanbadri99@gmail.com",
                "jobCategory": "Software-env",
                "jobTitle": "Test job",
                "companyName": "wilfrid-laurier",
                "startDate": "2001-01-01T05:00:00.000Z",
                "endDate": "2001-01-01T05:00:00.000Z",
                "city": "Kitchener",
                "country": "Canada",
                "jobResponsibilities": [
                    "hello world",
                    "hello world"
                ],
                "__v": 0
            }
        ],
        "projects": [
            {
                "_id": "65b9e6441045a22dc75bf254",
                "userEmail": "adnanbadri99@gmail.com",
                "projectCategory": "software-dev",
                "projectTitle": "hello world",
                "projectSubtitle": "python|java|c",
                "projectDescription": [
                    "lol",
                    "lol 2"
                ],
                "__v": 0
            },
            {
                "_id": "65d45881238cc1386cb17f09",
                "userEmail": "adnanbadri99@gmail.com",
                "projectCategory": "algebra",
                "projectTitle": "algebra",
                "projectSubtitle": "2012",
                "projectDescription": [
                    "i didn't do anything",
                    "lol"
                ],
                "__v": 0
            }
        ],
        "education": {
            "_id": "65d429669831c9686f2b3f55",
            "userEmail": "adnanbadri99@gmail.com",
            "degree": "hi",
            "school": "fds",
            "city": "dsaf",
            "country": "f",
            "startDate": "f",
            "endDate": "ee",
            "__v": 0
        }
    },
    {
        "_id": "65d694e2de448527eefc88a7",
        "jobs": [
            {
                "_id": "65b9e5681b42085b28185053",
                "userEmail": "adnanbadri99@gmail.com",
                "jobCategory": "fdsaf",
                "jobTitle": "hello",
                "companyName": "sdf",
                "startDate": "2001-01-01T05:00:00.000Z",
                "endDate": "2001-01-01T05:00:00.000Z",
                "city": "fdsf",
                "country": "dsf",
                "jobResponsibilities": [
                    "asdfa",
                    "asdf"
                ],
                "__v": 0
            },
            {
                "_id": "65ba22593af837a39e9e17b6",
                "userEmail": "adnanbadri99@gmail.com",
                "jobCategory": "Software-env",
                "jobTitle": "Test job",
                "companyName": "wilfrid-laurier",
                "startDate": "2001-01-01T05:00:00.000Z",
                "endDate": "2001-01-01T05:00:00.000Z",
                "city": "Kitchener",
                "country": "Canada",
                "jobResponsibilities": [
                    "hello world",
                    "hello world"
                ],
                "__v": 0
            },
            {
                "_id": "65ba23483af837a39e9e17ed",
                "userEmail": "adnanbadri99@gmail.com",
                "jobCategory": "research",
                "jobTitle": "USRA research",
                "companyName": "wilfrid-laurier",
                "startDate": "2024-01-09T00:00:00.000Z",
                "endDate": "2024-04-09T00:00:00.000Z",
                "city": "Kitchener",
                "country": "Canada",
                "jobResponsibilities": [
                    "studied algebra",
                    "studied graph theory",
                    "studied deez nuts"
                ],
                "__v": 0
            }
        ],
        "projects": [
            {
                "_id": "65b9e6441045a22dc75bf254",
                "userEmail": "adnanbadri99@gmail.com",
                "projectCategory": "software-dev",
                "projectTitle": "hello world",
                "projectSubtitle": "python|java|c",
                "projectDescription": [
                    "lol",
                    "lol 2"
                ],
                "__v": 0
            },
            {
                "_id": "65b9eb1f522da589f7446946",
                "userEmail": "adnanbadri99@gmail.com",
                "projectCategory": "fds",
                "projectTitle": "fds",
                "projectSubtitle": "fdsa",
                "projectDescription": [
                    "fasd"
                ],
                "__v": 0
            }
        ],
        "education": {
            "_id": "65d429989831c9686f2b3f57",
            "userEmail": "adnanbadri99@gmail.com",
            "degree": "sdf",
            "school": "fds",
            "city": "f",
            "country": "f",
            "startDate": "e",
            "endDate": "f",
            "__v": 0
        }
    }
]
}

response = requests.get(url, json=data)

if response.status_code == 200:
    # Request was successful
    response_data = response.json()
    # Process the response data here
    print(response_data)
else:
    # Request failed
    print("Request failed with status code:", response.status_code)