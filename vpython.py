# Vulnerable Python script

import os
import pickle
import subprocess

# 1. Hardcoded credentials
def login():
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "1234":
        print("Welcome admin!")
    else:
        print("Access denied.")

# 2. Using eval on user input (code injection risk)
def eval_input():
    user_code = input("Enter a Python expression: ")
    print("Result:", eval(user_code))  # Dangerous!

# 3. Using pickle.load on untrusted input (deserialization attack)
def load_data():
    filename = input("Enter filename to load data from: ")
    with open(filename, "rb") as f:
        data = pickle.load(f)  # Dangerous if attacker controls the file
    print("Data loaded:", data)

# 4. Shell command injection via subprocess with shell=True
def run_shell():
    cmd = input("Enter shell command: ")
    subprocess.run(cmd, shell=True)  # Dangerous!

# 5. Using weak cryptography (storing plaintext password)
def store_password():
    password = input("Enter new password: ")
    with open("password.txt", "w") as f:
        f.write(password)  # Plaintext storage!

if __name__ == "__main__":
    login()
    eval_input()
    load_data()
    run_shell()
    store_password()

