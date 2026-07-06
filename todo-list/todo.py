import os

tasks = []

def load():
    if not os.path.exists("tasks.txt"):
        return
    with open("tasks.txt", "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 2:
                tasks.append({"text": parts[0], "done": parts[1] == "True"})

def save():
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(f"{t['text']}|{t['done']}\n")

def show():
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        status = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {status} {t['text']}")

def add(text):
    tasks.append({"text": text, "done": False})
    save()
    print(f"Added: {text}")

def done(num):
    if 1 <= num <= len(tasks):
        tasks[num-1]["done"] = True
        save()
        print(f"Task {num} marked done.")
    else:
        print("Invalid number.")

def delete(num):
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num-1)
        save()
        print(f"Deleted: {removed['text']}")
    else:
        print("Invalid number.")

load()

while True:
    print("\n=== TODO LIST ===")
    show()
    cmd = input("\nCommand (add/done/del/quit): ").strip().lower()
    if cmd == "quit":
        break
    elif cmd.startswith("add "):
        add(cmd[4:])
    elif cmd.startswith("done "):
        try:
            done(int(cmd[5:]))
        except:
            print("Use: done <number>")
    elif cmd.startswith("del "):
        try:
            delete(int(cmd[4:]))
        except:
            print("Use: del <number>")
    else:
        print("Commands: add <task>, done <num>, del <num>, quit")
