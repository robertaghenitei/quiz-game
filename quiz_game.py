import requests
import pprint

def get_response():
    response = int(input("Please chose the number of the correct question: "))
    return response



def format_the_question(data):
    category = data[0]['category']
    difficulty = data[0]['difficulty']
    correct_answer = data[0]['correct_answer']
    all_answers = data[0]['incorrect_answers'] + [correct_answer]
    # print(all_answers)
    question = data[0]['question']

    print(f"This question is of {difficulty} difficulty:")

    print(f"{question}")
    

    for i, answer in enumerate(all_answers):
        print(f"{i}. {answer}")



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
    question = get_question_from_api()
    format_the_question(question)
    response = get_response()


if __name__ == "__main__":
    main()