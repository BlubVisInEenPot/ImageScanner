import os

def clear_log():
    with open("errors.txt", "wt") as f:
        f.write("")

def log_errors(exeption):
    with open("errors.txt", "at") as f:
        f.write(f"- {exeption}\n\n")

def check_log():
    with open("errors.txt", "rt") as f:
        if f.read() == "":
            return False
        else:
            return True


clear_log()
#
# for l in range(2):
#     log_errors(f"test{l}")

print(check_log())