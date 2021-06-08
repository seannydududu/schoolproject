#strings For-loops and Indexing
def jumble():
    #initialising
    list = []
    word = ""
    while_counter = 0
    #prompts for user's input
    user_input = input("Enter a word:")
    #makes the user_input into a list
    for letters in user_input:
        list += letters
    # if user's input is a even number of letters it will jumble by swapping the consecutive pairs of letters
    if len(user_input) % 2 == 0:
        total_pairs = len(user_input) / 2
        while while_counter < total_pairs:
            word += list.pop(1)
            word += list.pop(0)
            while_counter +=1
    # if user's input is a odd number of letters it will jumble by swapping the consecutive pairs of letters
    # and will leave the last letter the same
    if len(user_input) % 2 == 1:
        total_pairs = (len(user_input) / 2) - 0.5
        while while_counter < total_pairs:
            word += list.pop(1)
            word += list.pop(0)
            while_counter += 1
        word += list[0]
    print(word)
#Lists , For-loops and Indexing
def score():
    #initialising
    subjects = ['English','Math','Science','Humanitites']
    student_counter = 1
    total_score = 0
    english_counter = 0
    subject_counter = 0
    database = [[56,78,80,65],[77,46,34,66],[43,67,45,39],[59,53,44,55]]
    #outputs the humanities score of student 3
    print("Student 3 Humanities Score is {}".format(database[2][3]))
    #all the scores for student 1
    for score in database[0]:
        print("Student 1 {} score is {}".format(subjects[subject_counter],score))
        subject_counter+=1
    #average score for English amongst the 4 students
    while english_counter < 4:
        total_score += database[english_counter][0]
        english_counter +=1
    total_score = total_score /4
    print("Average score for English is {}".format(total_score))
    total_score = 0
    #Outputs the Average score of the 4 students
    for student in database:
        for stu in student:
            total_score += stu
        total_score = total_score / 4
        print("Average score for student {} is {}".format(student_counter,total_score))
        total_score = 0
        student_counter += 1
score()

