# Quiz-Game

This code initializes and runs a quiz application by integrating question data, quiz logic, and a graphical user interface (GUI). It first imports necessary classes and data, including Question for handling individual questions, question_data which contains the list of questions fetched from an external source, QuizBrain for managing the quiz logic, and QuizInterface for creating the user interface.

The code then constructs a question_bank, which is a list of Question objects. Each Question object is created using the text and correct answer from the question_data. This list of questions is passed to the QuizBrain instance, which is responsible for managing the quiz flow.

Finally, the QuizInterface is initialized with the QuizBrain instance, launching the quiz in a graphical window. After the user completes the quiz, the program prints a message indicating the end of the quiz and displays the user's final score in the console. This structure effectively combines the backend logic and frontend interface to create a complete quiz application.

# UI.py
- I used a GUI called tkinter to allow the user to interact with the quiz.
 
# In the class Initialization (__init__):
  
- Initializes the main window with a title and background color.
- Sets up a label to display the score.
- Creates a canvas to display quiz questions.
- Adds two buttons (True/False) with images to allow the user to answer questions.
- Calls the get_next_question method to load the first question.

# get_next_question():

- Updates the quiz question on the canvas or displays a message if there are no more questions.
- Updates the score label with the current score.

- Button Press Methods (true_pressed and false_pressed):

- Handle user input for True and False answers, check if the answer is correct, and then give feedback.

# give_feedback():

- Provides visual feedback by changing the canvas color to green (correct) or red (incorrect).
- Moves on to the next question after a brief delay.

# QUIZ_BRAIN.py

- In the class Initialization (__init__):

- Takes a list of questions (q_list) and initializes the question number, score, and the current question.

- still_has_questions():

- Checks if there are any questions left to ask by comparing the current question number with the length of the question list.

- next_question():

- Retrieves the next question from the list, increments the question number, and returns the question text after unescaping any HTML entities to avoid running into errors.

- check_answer():

- Compares the user's answer with the correct answer (case-insensitive). If correct, it increments the score and returns True; otherwise, it returns False

# DATA.py
- This file is used to extract code from the 'Open Trivia Database' API.

- Parameters:
  
- amount: Specifies the number of quiz questions to fetch (10 in this case).
- type: Sets the type of questions to "boolean" (True/False).

- API Endpoint:
  - The api_endpoint variable stores the URL for the Open Trivia Database API

- requests.get sends an HTTP GET request to the API with the specified parameters.
- response.raise_for_status() checks for any HTTP errors (e.g., 404 or 500) and raises an exception if any are found.
- The response is parsed as JSON, and the list of questions is accessed via response.json()["results"] and stored in the question_data variable.
- This question_data list will contain the quiz questions and their corresponding answers, which will then be used by the QuizBrain class/








  
