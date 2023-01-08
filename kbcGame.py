# Kaun Banega Crorepati

print("\n*** Rules For Playing the game ***\n")
print("~ There are 15 questions in the game")
print("~ Each question have 4 options")
print("~ Out of 4 only one option is correct")
print("~ By giving each correct answer you will win the assigned value of points with it")
print("~ If you give the wrong answer you will be eleminated from the game")
print("~ Game has two safety points")
print("~ First at 5th question and Second at 10th question which assures you that you win that much amount of money when you clear those questions")
print("~ If you stuck in the game you can also exit the game at that point by giving -1 as answer and you will win the amount you have earned\n")

start = input("Press enter to start the game\n")

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000,
          160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

questions = [
    ["What is Capital of Madhaya Pradesh",
        "Indore", "Gwalior", "Bhopal", "Sanchi", 3],

    ["Which Day we celebrate Children's Day in India?",
        "25 September", "14 November", "5 September", "15 August", 2],

    ["How many consonants are there in the English alphabet?", "26", "5", "22", "21", 4],

    ["Name the National fruit of India?", "Banana", "Mango", "Apple", "Sitafal", 2],

    ["Name the densest jungle in the world?", "The Amazon rainforest",
        "Tropical rainforest in Borneo", " The Taiga", "Burmese Tropical Rainforest", 1],

    ["Name the smallest continent?", "Australia",
        "Antartica", "Japan", "Srilanka", 1],

    ["Name the National game of the USA?", "Basketball",
        "Rugby", "Baseball", "Football", 3],

    ["Who among the following wrote Sanskrit grammar?",
        "Kalidasa", "Charak", "Panini", "Aryabhatt", 3],

    ["The metal whose salts are sensitive to light is?",
        "Silver", "Zinc", "Copper", "Aluminium", 1],

    ["Which one of the following ports is the oldest port in India?",
        "Mumbai Port", "Chennai Port", "Kolkata Port", "Vishakhapatnam Port", 2],

    ["At which one of the following places do the rivers Alaknanda and Bhagirathi merge to form Ganga?",
        "Rudra Prayag", "Karnaprayag", "Vishnuprayag", "Devprayag", 4],

    ["FFC stands for", "Federation of Football Council", "Foreign Finance Corporation",
        "Film Finance Corporation", "None of the above", 3],

    ["First China War was fought between", "China and Egypt",
        "China and Greek", "China and Britain", "China and France", 3],

    ["Golf player Vijay Singh belongs to which country?",
        "India", "Fiji", "UK", "Scotland", 2],

    ["Epsom (England) is the place associated with",
     "Shooting", "Polo", "Snooker", "Horse racing", 4],
]

amount = 0
quitflag = False

i = 0
for i in range(len(questions)):
    question = questions[i]
    
    print(f"({i+1}) Question for Rs. {levels[i]} is :-")
    print(question[0])
    print(f"1. {question[1]}        2. {question[2]}")
    print(f"3. {question[3]}        4. {question[4]}")
    answer = int(input("Enter a answer : "))
    
    if (answer == question[5]):
        print(f"You won Rs.{levels[i]}")
        amount = levels[i]

    elif (answer == -1):
        amount = levels[i-1]
        quitflag = True
        break

    else:
        break

    print("\n")

if quitflag == False:
    if (amount < 10000):
        amount = 0
    elif (amount >= 10000 and amount < 320000):
        amount = 10000
    elif (amount >= 320000 and amount < 10000000):
        amount = 320000
    elif (amount == 10000000):
        amount = 10000000

print(f"\nTotal Amount You Won is Rs.{amount}")
