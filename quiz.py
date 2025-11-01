print("Welcome in python")
first_name = input("Enter your first name: ")
first_name = str(first_name)
user = input("Enter your name: ")
user = str(user)
age = input("Enter your age: ")
age = str(age)
if first_name == 'Bangaly' and user == 'Kaloka':
    print(f"Welcome in python {first_name} {user} ")
else:
    print("Okay you are not creator, are you ready for quiz")
print("Let's go ")
print("")
accord_first = input("Enter yes or no for continuous: ")
accord_first = str(accord_first)
if accord_first == 'yes':
    print("""First question,Who is that the first president of Malia.
 -1 Modibo Keïta
 -2 Alassane Ouattara
 -3 Ibrahima boubacar Keïta""")
else:
    print(f"Leave the script {user} or continuous")
answer_first = input("Enter your answer(1,2,3): ")
answer_first = int(answer_first)
if answer_first == 1:
    print(f"Good answer {first_name} {user}")
elif answer_first == 2:
    print("oh no bad answer")
else:
    print("oh no bad answer repeat")
print("Continuous the quiz answer with(yes or no)")
accord_second = input("Enter yes or no: ")
accord_second = str(accord_second)
if accord_second == 'yes':
    print("Okay continuous the second question bro")
else:
    print("Okay leave the script contact the support for more information")
print("Second question are you ready")
accord_second = input("Enter yes or no for continuous: ")
accord_second = str(accord_second)
if accord_second == 'yes':
    print("""Second question Give the device of Malia
    -1 Un Peuple,Un But,Une Foi
    -2 Travail,Discipline,Réussite
    -3 Une Nation,Un But,Developpement""")
else:
    print("okay you can leave")
answer_second = input("Enter your response(1,2,3): ")
answer_second = int(answer_second)
if answer_second == 1:
    print(f"Good answer {first_name} {user} continue comme ça mec")
elif answer_second == 2:
    print("oh no bad answer repeat again")
else:
    print("oh no bad answer again")
print(" ")
print("Are you ready for tree question")
accord_tree = input("Enter yes or no for continuous: ")
accord_tree = str(accord_tree)
if accord_tree == 'yes':
    print("""Tree question: who is that rhe actually president of Ivory coast
    -1 Assimi Koïta
    -4 Kankou Moussa
    -8 Alassane Ouattara""")
else:
    print("Okay you can leave the quiz")
answer_tree = input("Enter your answer with (1,4,8): ")
answer_tree = int(answer_tree)
if answer_tree == 1:
    print("oh no bad response")
elif answer_tree == 4:
    print("oh no Sir bad answer repeat")
elif answer_tree == 8:
    print("Goooooood response sir")
else:
    print("ERROR repeat the quiz")





