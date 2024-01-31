date = input("Enter today's date: ")
mood = input("How do you rate your mood today? From 1 to 10: ")
thoughts = input("Let your thoughts flow:\n")

with open(f"report.txt", 'w') as file:
    file.write(date + "\n" + mood + 2 * "\n")
    file.write(thoughts)