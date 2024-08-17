# Quiz-Game

- Quiz game that extracts data from the 'Open Trivia Database' through calling an api with specific parameters of what type of questions I want. In this case I asked for 10 questions, with a boolean type.

- I used multiple files to handle a specific part of the project.

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
  
amount: Specifies the number of quiz questions to fetch (10 in this case).
type: Sets the type of questions to "boolean" (True/False).










  
