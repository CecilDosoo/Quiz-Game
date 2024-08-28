# Quiz Game

This project is a simple Quiz Game application built using Python. It integrates question data from an external API, manages quiz logic, and provides a graphical user interface (GUI) using Tkinter.

https://github.com/user-attachments/assets/071a3ab9-df68-4771-b637-ab24d9b32b07


## Table of Contents
- [main.py](#mainpy)
- [ui.py](#uipy)
- [quiz_brain.py](#quiz_brainpy)
- [data.py](#datapy)
- [question_model.py](#questionmodelpy)

## main.py

The `main.py` file initializes and runs the quiz program by integrating the question data, quiz logic, and GUI.

### Key Components:
- **Imports**: 
  - `Question`: Handles individual questions.
  - `question_data`: Contains the list of questions fetched from an external source.
  - `QuizBrain`: Manages the quiz logic.
  - `QuizInterface`: Creates the user interface.

### Workflow:
1. **Question Bank**: 
   - Constructs a `question_bank` list, where each item is a `Question` object created using text and correct answer from `question_data`.
   
2. **QuizBrain**:
   - Manages the quiz flow by receiving the `question_bank`.

3. **QuizInterface**:
   - Launches the quiz in a graphical window, interacting with `QuizBrain`.

4. **Completion**:
   - Once the quiz ends, it prints a message and displays the user’s final score in the console.
   - ![image](https://github.com/user-attachments/assets/fad8778f-a80f-406a-afba-4ecfffe9177b)
## ui.py

The `ui.py` file is responsible for the graphical user interface (GUI) using Tkinter.

![image](https://github.com/user-attachments/assets/48a24ef5-1ca1-4fec-8230-3758dd5935e4)

### Key Components:
- **Initialization (`__init__`)**:
  - Initializes the main window with a title and background color.
  - Sets up a label to display the score.
  - Creates a canvas to display quiz questions.
  - Adds two buttons (True/False) with images for user interaction.
  - Calls `get_next_question` to load the first question.

- **get_next_question()**:
  - Updates the quiz question on the canvas.
  - Updates the score label or displays a message if there are no more questions.

- **Button Press Methods (`true_pressed` and `false_pressed`)**:
  - Handle user input for True and False answers.
  - Check if the answer is correct and give feedback.
  - ![image](https://github.com/user-attachments/assets/33fbbea1-fd76-4e5a-a31d-09dc0b8950f4)
  - ![image](https://github.com/user-attachments/assets/0e81a21a-827d-4472-92ed-f1161e7e6eb9)

- **give_feedback()**:
  - Provides visual feedback by changing the canvas color to green (correct) or red (incorrect).
  - Moves to the next question after a brief delay.

## quiz_brain.py

The `quiz_brain.py` file contains the `QuizBrain` class, which manages the quiz's logic.

### Key Components:
- **Initialization (`__init__`)**:
  - Takes a list of questions (`q_list`) and initializes the question number, score, and the current question.

- **still_has_questions()**:
  - Checks if there are any remaining questions.

- **next_question()**:
  - Retrieves the next question, increments the question number, and returns the question text after unescaping any HTML entities.

- **check_answer()**:
  - Compares the user's answer with the correct answer (case-insensitive).
  - If correct, increments the score and returns `True`; otherwise, returns `False`.

## data.py

The `data.py` file is used to extract question data from the Open Trivia Database API.

### Key Components:
- **Parameters**:
  - `amount`: Specifies the number of quiz questions to fetch (10 in this case).
  - `type`: Sets the type of questions to "boolean" (True/False).

- **API Endpoint**:
  - The `api_endpoint` variable stores the URL for the Open Trivia Database API.

- **HTTP Request**:
  - `requests.get` sends an HTTP GET request to the API with the specified parameters.
  - `response.raise_for_status()` checks for any HTTP errors and raises an exception if found.
  - The response is parsed as JSON, and the list of questions is accessed via `response.json()["results"]` and stored in the `question_data` variable.

This `question_data` list contains the quiz questions and their corresponding answers, which are used by the `QuizBrain` class.

## question_model.py

The `question_model.py` file contains the `Question` class, which is used to create question objects in the quiz.

### Key Components:
- **Initialization (`__init__`)**:
  - The `Question` class takes two arguments: `q_text` (the text of the question) and `q_answer` (the correct answer).
  - These are stored in the `text` and `answer` attributes of the class, respectively.

This class serves as a simple model to encapsulate the data for each quiz question, making it easier to manage and use within the `QuizBrain` class.
