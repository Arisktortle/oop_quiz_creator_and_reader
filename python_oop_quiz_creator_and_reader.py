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
    
def write_question_to_file(question_data, filename="quiz_data.txt"): #export the data of the questions inputted into a file
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"#QUESTION_{question_data['number']}_START\n")
        f.write(f"Question {question_data['number']}: {question_data['question']}\n")
        for opt in ['a', 'b', 'c', 'd']:
            f.write(f"{opt}) {question_data['choices'][opt]}\n")
        f.write(f"ANSWER: {question_data['correct']}\n")
        f.write(f"#QUESTION_{question_data['number']}_END\n\n")

#reads how many questions inputted
def get_existing_question_count(filename="quiz_data.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        count = sum(1 for line in lines if line.strip().startswith("#QUESTION_") and "_START" in line) #reads the number of questions and stores the count
        return count
    except FileNotFoundError:
        return 0
    
#welcome menu for quiz and calls all three functions
def main():
    print("Welcome to Quiz Creator Program!")

    while True:
        try:
          number_of_questions = int(input("Enter how many questions to input: ")) #numbers of questions to be entered
          if number_of_questions > 0: #checks if the value inputted is valid
             break
          else:
            print("Enter a valid number greater than 0.") 
        except ValueError: 
            print("Invalid number input.")
            
    starting_number = get_existing_question_count() + 1

    for i in range(number_of_questions):
        question_number = starting_number + i
        question_data = user_questions(question_number)
        write_question_to_file(question_data)
        print(f"\nInputted question {question_number} saved.\n")
        
    print(f"{number_of_questions} question(s) added and exported to file.\n")
    
if __name__ == "__main__":
    main()