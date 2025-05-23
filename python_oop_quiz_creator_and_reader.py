#prompt the user for question and choices
def user_questions(number): 
    print(f"For question {number}")
    question = input("Enter your question:\n ").strip() #asks the user for questions
    
    print("\n Enter the choices: ") #prompts the user to enter choices
    choices = {}
    for option in ['a', 'b', 'c', 'd']: #chooses questions between a, b, c, and d
        answer = input(f" {option}) ").strip()
        choices[option] = answer
        
    while True:
        correct_answer = input("\n Select the correct answer: (a, b, c, d,: )").lower() #inputs the correct answer and stores
        if correct_answer in choices:
            break
        else:
         print("Invalid option. Select from (a, b, c, d,).") #checks if the correct answer entered is valid
    
    return { #dictionary to access the questions, choices and the correct answer easily
        "number": number, 
        "question": question,
        "choices": choices,
        "correct": correct_answer
    }     
        
#export the questions inputted into a file
#reads how many questions inputted
#welcome menu for quiz and calls all three functions