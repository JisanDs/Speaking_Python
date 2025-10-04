"""🔄 পরিবর্তন করি Day 39 কে একটু advanced করে:

🧠 Day 39 – Speak Python 28 (Advanced Version)

Phase 7: Real-World Thinking (Recursion + Data Structures + OOP + Debugging + Mini Project)"""


"""✅ Problem Set (New & Different)

🔁 Recursion (2 problems – নতুন ধরণের)

1. Nested Sum (Recursive)
Write a recursive function to calculate the sum of all numbers inside a nested list.

Input: [1, [2, [3, 4], 5], 6]
Output: 21"""

def nest_lst_sum(lst):
    total = 0
    for n in lst:
        if isinstance(n, list):
            total += nest_lst_sum(n)
        else:
            total += n
    return total

print(nest_lst_sum([1, [2, [3,[3,[8, 9], 5], 4], 5], 6]))

"""2. Directory Traversal (Recursive)
Simulate a recursive function that prints all files in a nested dictionary structure.



files = {
    "root": {
        "docs": {"a.txt": None, "b.txt": None},
        "images": {"photo.png": None, "logo.jpg": None},
        "src": {
            "main.py": None,
            "utils": {"helper.py": None}
        }
    }
}

Output:

root/docs/a.txt
root/docs/b.txt
root/images/photo.png
root/images/logo.jpg
root/src/main.py
root/src/utils/helper.py"""



def dir_traverse(diractory, path=""):
    for name, cont in diractory.items():
        new_path = f"{path}/{name}" if path else name
        
        if isinstance(cont, dict):
            dir_traverse(cont, new_path)
        else:
            print(new_path)


files = {
    "root": {
        "docs": {"a.txt": None, "b.txt": None},
        "images": {"photo.png": None, "logo.jpg": None},
        "src": {
            "main.py": None,
            "utils": {"helper.py": None}
        }
    }
}

# dir_traverse(files)


# ⚡ Other Concepts (2 problems – নতুন ধরণের)

"""3. Set Operations
Given two sets:



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

Find:

Union
Intersection
Difference (A - B)"""

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# builtin method
def main():
    print(A.union(B))
    print(A.intersection(B))
    print(A.difference(B))
# main()

# my wone
def my_union(a, b) -> set:
    un = []
    for n in a:
        if n not in un:
            un.append(n)
    for n in b:
        if n not in un:
            un.append(n)
    return set(un)
        

def my_itst(a, b) -> set:
    un = []
    for n in a:
        if n in a and n in b:
            un.append(n)
    for n in b:
        if n in a and n in b:
            un.append(n)
    return set(un)


def diff_set(a, b):
    diff = []
    for n in a:
        if n not in b:
            diff.append(n)
    return set(diff)


# print(my_union(A, B))
# print(my_itst(A, B))
# print(diff_set(A, B))

"""4. Frequency Counter (Dictionary)
Write a function that counts the frequency of each character in a string.

Input: "programming"
Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}"""

def frq_counter(s) -> str:
    frq = {}
    for char in s:
        frq[char] = frq.get(char, 0) + 1
    return frq

# print(frq_counter("jjijsadjfsaldfjsa"))
# print(frq_counter("programming"))


"""🛠️ Debugging Task (নতুন)

Buggy code:

class BankAccount:
    def __init__(self, balance):
        balance = balance
    
    def deposit(self, amount):
        self.balance += amount

acc = BankAccount(100)
acc.deposit(50)
print(acc.balance)  # Expected: 150

👉 Fix the error so it works correctly."""

# fixed code:
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

acc = BankAccount(100)
acc.deposit(50)
# print(acc.balance)  # Expected: 150



"""📂 Mini Project – Password Manager (OOP + File Handling)

Features:

add_password(service, password) → save a password for a service
view_passwords() → display all saved passwords
remove_password(service) → delete password for a service

Save all data in passwords.json"""

from file_utilites import save_json, load_json


class PasswordManager:
    def __init__(self, file="passwords.json"):
        self.file = file
        self.passwords = load_json(self.file)

    def add_password(self, service, password):
        if service not in self.passwords:
            self.passwords[service] = password
            save_json(self.passwords, self.file)
        else:
            print(f"{service} alredy exist")

    def view_passwords(self):
        if self.passwords:
            for i, (serv, pas) in enumerate(self.passwords.items(), start=1):
                print(f"{i}. {serv}: {pas}")
        else:
            print(f"Password manager are empty")

    def update_password(self, serv, new_pas):
        if serv in self.passwords:
            self.passwords[serv] = new_pas
            save_json(self.passwords, self.file)
        else:
            print(f"{serv} not exist")

    def remove_password(self, serv):
        if serv in self.passwords:
            del self.passwords[serv]
            save_json(self.passwords, self.file)
        else:
            print(f"{serv} not exist")


# test's
# pm = PasswordManager()
# pm.add_password("email", "jisanpanda")
# pm.add_password("facebook", "panda_980")
# pm.add_password("twitter", "check_hello")
# pm.view_passwords()
# pm.update_password("email", "hello_jisan")
# pm.view_passwords()

# pm.remove_password("twitter")
# pm.view_passwords()


# small project

def main():
    pm = PasswordManager()
    
    while True:
        print("___Menu Bar___")
        print("1. Add")
        print("2. Remove")
        print("3. Update")
        print("4. View")
        print("5. Exit")
        choise = int(input("Opsion: "))

        if choise == 1:
            service = input("Enter servies name: ")
            password = input("Enter your password: ")
            pm.add_password(service, password)

        elif choise == 2:
            service = input("Enter servies name: ")
            pm.remove_password(service)

        elif choise == 3:
            service = input("Enter servies name: ")
            new_password = input("Enter your password: ")
            pm.update_password(service, new_password)

        elif choise == 4:
            pm.view_passwords()

        elif choise == 5:
            break

        else:
            print("Error: Invalid choise")
    
# if __name__ == "__main__":
#     main()