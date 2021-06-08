#Question 1
def qn1():
    name = input("Enter your name:")
    index = input("Enter your index number:")
    class_name = input("Enter your class:")
    print("Hi, I am {} from class {} and my index number is {}.\nNice to meet you.".format(name,class_name,index))
#Question3
def qn3():
    counter = 0
    total = 0
    user_input = int(input("Enter a multiplication factor:"))
    while counter < 11:
        total = counter * user_input
        print("{} x {} = {}".format(counter,user_input,total))
        counter += 1
        total = 0
#Question 5
def qn5():
    user_input = input("Enter your name: ")
    if 'z' in user_input:
        print("Your a BAD person.")
    else:
        print("Your a GOOD person.")
#Question 6
def qn6():
    user_input = input("Enter a sentence:")
    user_input = user_input.replace(" ","")
    print(user_input)
#quesion 7
def qn7():
    count = 1
    word = ""
    user_input = input("Enter a word:")
    user_input2 = input("a)iteration or b)indexing")
    if user_input2 == "a":
        for letters in user_input:
            word += user_input[-count]
            count += 1
        print(word)
    if user_input2 == 'b':
        print(user_input[::-1])
#Question 8
def qn8():
    user_input = input("Enter a phrase")
    print(user_input.title())
#Question 9
def qn9():
    word = ""
    user_input = input("Enter a sentence:")
    splited = user_input.split()
    reversed_sentence = ' '.join(reversed(splited))
    print(reversed_sentence)




