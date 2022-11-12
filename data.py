import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

data = response.json()
question_data = data["results"]

# question_data = [{"question": h.unescape(each["question"]), "correct_answer": each["correct_answer"]}
#                  for each in data]
