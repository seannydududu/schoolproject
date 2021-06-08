#Question 1
def qn1():
    scrabble_score = 0
    #list of scoring tables
    score1 = ['a','e','i','l','n','o','r','s','t','u']
    score2 = ['d','g']
    score3 = ['b','c','m','p']
    score4 = ['f','h','v','w','y']
    score5 = ['k']
    score6 = ['j','x']
    score7 = ['q','z']
    #prompts the user's input
    user_input = input("Enter a word:")
    #awards the point to the letters and stores it in scrabble score
    for letters in user_input:
        if letters in score1:
            scrabble_score +=1
        elif letters in score2:
            scrabble_score += 2
        elif letters in score3:
            scrabble_score += 3
        elif letters in score4:
            scrabble_score += 4
        elif letters in score5:
            scrabble_score += 5
        elif letters in score6:
            scrabble_score += 8
        else:
            scrabble_score += 10
    #prints the scrabble score
    print("Your scrabble score is {}.".format(scrabble_score))
#Question 2
def qn2():
 #asks for user_input
 user_input = input("Enter a word : ")
 occurance = {}
 high = 0
 #for loop
 for letters in user_input:
  # if letter is inside dictionary,its value +=1 , else , it will make a new key,value in dictionary
  try:
    occurance[letters] += 1
  except:
    occurance[letters] = 1
 #for loop to check the highest value
 for highest in occurance.values():
    if highest > high :
        high = highest
 #for loop to call for the key of the highest value
 for key,value in occurance.items():
    if high == value:
        #prints out the statement
        print("{0} occurs {1} times.".format(key,value))
#Question 3
def qn3():
    end = ""
    #alphabet list is initiated in alphabetical order
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    user_input = input("Enter a word: ")
    for letter in user_input:
        #plus 1 because the first index is 0 and the encoding starts with a:1
        index = alphabet_list.index(letter) +1
        end += " "+ str(index)
    print(end)
#Question 4
def qn4():
    end = ""
    occurances = {}
    #asks the user's input
    user_input = input("Enter a chemical formula: ")
    #loops through every letter in user's input
    for letters in user_input:
        #if letter is not inside dictionary , it will add a key:value into dictionary
        #Else it will add 1 to the value inside the dictionary
        try:
            occurances[letters] += 1
        except:
            occurances[letters] = 1
    #prints the statement
    for key,value in occurances.items():
        end += str(key)+str(value)
    print(end)
#Question 5
def qn5():
    #initialising variables
    printing = ""
    unsorted_list = []
    sorted_list = []
    #user_input
    user_input = input('Enter a word:')
    #putting the user's input from a string into a list format
    for letters in user_input:
        unsorted_list += letters
    #A while loop to sort the string into alphabetical order until everything in the sorted list is gone
    #keeps finding the smallest value in alphabetical order until everything in the list is gone
    while unsorted_list:
        smallest = min(unsorted_list)
    #adds the item to the sorted list
        sorted_list.append(smallest)
        #.pop() removes the item from the list
        unsorted_list.pop(unsorted_list.index(smallest))
    for letters in sorted_list:
        printing += letters
    #prints the sorted list in a string format
    print(printing)
#Question 6
def qn6():
    #prompts the user's name
    user_input = input("Enter Your Name:")
    #basically vowels
    vowels = ['a','e','i','o','u']
    #if user name ends with a vowel it will add a z
    #else it will add a y
    if user_input[len(user_input)-1] in vowels:
        print(user_input + "z")
    else:
        print(user_input + "y")
#Question 7
def qn7():
    hash = 0
    count = 1
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    user_input = input("Enter a word: ")
    index = alphabet_list.index(user_input[0]) + 1
    hash += index
    #adds every first number in a pattern
    for letters in user_input[1::]:
     if (user_input.find(user_input[count])+1) % 2 == 0:
        # plus 1 because the first index is 0 and the encoding starts with a:1
        index = alphabet_list.index(letters) + 1
        hash += index
        count +=1
    # adds every second number in a pattern
     elif (user_input.find(user_input[count])+1) % 2 == 1:
        # plus 1 because the first index is 0 and the encoding starts with a:1
        hash = (alphabet_list.index(letters) + 1) * hash
        count+=1
    hash = str(hash)
    print(hash[-4:])




