#function to break the sentence

def Break_Sentence(sentence):
    words = [] 
    word = ''
    for i in range(0,len(sentence)):
        if sentence[i] == ' ' or i == len(sentence)-1:
            if i == len(sentence)-1:
                word += sentence[i]
            words.append(word)
            word = ''
        else:
            word += sentence[i]
    return words

#function to store all the duplicate words at once in a uniqu_list
def unique_list(words):
    unique_list = []

    for i in words:
        isUnique = True
        for j in unique_list:
            if i == j:
                isUnique = False
        if isUnique == True:
            unique_list.append(i)
    return unique_list

#function to count the occurance of a word
def Word_Counter(words,unique_list):
    for i in unique_list:
        count = 0
        for j in words:
            if i == j:
                count = count + 1
        print(f"word - {i}  | count - {count}")


#user manual 
print("Select your choice : ")
print("1: word-counter ")
print("2 : Exit ")
while True:
    choice = int(input("Your Choice : "))
    if choice == 1:
        userInput = input("Enter your sentence : ")
        words = Break_Sentence(userInput)
        unique = unique_list(words)
        Word_Counter(words,unique)
    else:
        print("Exit : ")
        break
   