#prompt the user for question and choices
def user_questions(number): 
    print(f"For question {number}")
    question = input("Enter your question:\n ").strip() #asks the user for questions
    
    print("\n Enter the choices: ") #prompts the user to enter choices
    choices = {}
    for option in ['a', 'b', 'c', 'd']: #chooses questions between a, b, c, and d
        answer = input(f" {option}) ").strip()
        choices[option] = answer
        
#export the questions inputted into a file
#reads how many questions inputted
#welcome menu for quiz and calls all three functions