import requests
import pprint #used this to see the response 
import random
import html #sometimes the api uses &quot, &#039 so we use this to unencode the answer  

def get_response():
    try:
        response = int(input("Please chose the number of the correct question:(1-4) "))
        if 1 <= response <= 4:
            return response - 1
        else:
            print("Invalid answer. You must chose a number between 1 - 4")
            return get_response()
    except ValueError:
        print("Invalid answer. You must chose a number between 1 - 4")
        return get_response()
    



def format_the_question(data):
    category = data[0]['category']
    difficulty = data[0]['difficulty']
    correct_answer = html.unescape(data[0]['correct_answer'])
    all_answers = [html.unescape(ans) for ans in data[0]['incorrect_answers']] + [correct_answer]
    # print(all_answers)
    question = html.unescape(data[0]['question'])

    print(f"This question is of {difficulty} difficulty:")

    print(f"{question}")
    
    random.shuffle(all_answers)

    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")
    return [all_answers, correct_answer]


def get_question_from_api():
    URL = "https://opentdb.com/api.php?amount=10&type=multiple"
    PARAMS = {"amount": 1, "type": "multiple"}
    try:
        response = requests.get(url=URL, params=PARAMS)
        
        if response.status_code == 200:
            # print("Request was successfull")
            data = response.json()['results']
            # pprint.pprint(data)
            return data
        else:
            print("Request was not successfull")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def main():   
    score = 0
    while True:
        question = get_question_from_api()
        answers = format_the_question(question)
        response = get_response()
        if answers[0][response] == answers[1]:
            print("Correct")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {answers[1]}")
        print("Score =", score)
        finish = input("Do you wanna continue? (y/n):")
        if finish == "n":
            break
        
if __name__ == "__main__":
    main()