# Welcome to quiz game

print("\nWELCOME TO KBL\n")
print("You can win 100,000 rupees from here if you answer all the quiz questions correctly.")
print("Here is some quizz")

# Questions for quiz

questions = ["1. What is the output of 3 + 2 * 2 in Python?",
             "2. Which of the following functions is used to get the length of a list in Python?",
             "3. Which operator is used to check if two values are not equal in Python?",
             "4. Which planet is known as the Red Planet?",
             "5. How many continents are there on Earth?",
             "6. What is the largest mammal in the world?",
             "7. What is the primary language spoken in Brazil?",
             "8. What is the largest ocean on Earth?",
             "9. Which animal is known as the \"King of the Jungle\"?",
             "10. What is the hardest natural substance on Earth?",
             "11. What is the largest planet in our solar system?",
             "12. What is the largest desert in the world?",
             "13. Which vitamin is produced when a person is exposed to sunlight?",
             "14. How many teeth does an adult human typically have?",
             "15. Which planet is closest to the sun?",
             "16. Which organ is responsible for detoxifying chemicals and metabolizing drugs in the human body?",
             "17. How many colors are there in a rainbow?",
             "18. What is the boiling point of water at sea level?",
             "19. What is the tallest mountain in the world?",
             "20. How many hearts does an octopus have?"]

# Choices for quiz

choices = [
    ["A. 10", "B. 7", "C. 8", "D. 6"],
    ["A. count()", "B. length()", "C. size()", "D. len()"],
    ["A. <>", "B. =", "C. !=", "D. =="],
    ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. 5", "B. 6", "C. 7", "D. 8"],
    ["A. Elephant", "B. Blue Whale", "C. Giraffe"],
    ["A. Spanish", "B. Portuguese", "C. French", "D. English"],
    ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
    ["A. Lion", "B. Tiger", "C. Leopard", "D. Cat"],
    ["A. Gold", "B. Diamond", "C. Obsidian","Silver"],
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. Sahara Desert", "B. Gobi Desert", "C. Arabian Desert", "D. Antarctic Desert"],
    ["A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"],
    ["A. 28", "B. 30", "C. 32", "D. 34"],
    ["A. Earth", "B. Venus", "C. Mercury", "D. Mars"],
    ["A. Heart", "B. Lungs", "C. Liver", "D. Kidneys"],
    ["A. 5", "B. 6", "C. 7", "D. 8"],
    ["A. 90°C", "B. 100°C", "C. 110°C", "D. 120°C"],
    ["A. Mount Kilimanjaro", "B. K2", "C. Mount Everest", "D. Mount Fuji"],
    ["A. 1", "B. 2", "C. 3", "D. 4"]
]

# Correct answers of quiz

correct_answers = ["B", "D", "C", "B", "C", "B", "B", "D", "A", "B", "C", "D", "D", "C", "C", "C", "C", "B", "C", "C"]

# Now quiz starts

prize_money = 5000
total_winnings = 0

for q in range(len(questions)):
    print("\n" + questions[q]+"\n")

    for choice in choices[q]:
        print(choice)

    print("\n""Enter you answer from A,B,C,D")
    ans = input("Your answer : ").upper()
    
    if ans == correct_answers[q]:
        print("\n""Yes that's correct answer")
        print("You won " , prize_money)
        total_winnings += prize_money
    else:
        print("Sorry but that's not a correct answer")
        print("The correct answer is " , correct_answers[q])

print("\n""NOW QUIZ IS OVER !")
print("Congrates you won ",total_winnings,"in the prize money")

# Now Quiz is end



    
    

