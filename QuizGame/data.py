import requests
import random

"""
You may choose the difficulty or keep as random using random choice with DIFFICULTY list.
You may add a category parameter choose the category from the range of 9 - 32 
or keep as random using randint. However some categories do not support some difficulty stage.
"""
DIFFICULTY = ["easy", "medium", "hard"]
parameters = {
    "amount": 10,
    "type": "boolean",
    "difficulty": random.choice(DIFFICULTY),
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
