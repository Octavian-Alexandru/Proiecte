import os
import json

# Clasa Task pentru a modela fiecare task
class Task:
    def __init__(self, title, description, status="Pending"):
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

# Clasa TaskManager pentru a gestiona task-urile
class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    # Încarcă task-urile din fișier
    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        return []

    # Salvează task-urile în fișier
    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)

    # Adaugă un task nou
    def add_task(self, task):
        self.tasks.append(task.to_dict())
        self.save_tasks()

    # Afișează toate task-urile
    def view_tasks(self):
        if not self.tasks:
            print("Nu există task-uri.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task['title']} - {task['status']}\n   {task['description']}")

    # Editează un task
    def edit_task(self, index, title=None, description=None, status=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index]['title'] = title
            if description:
                self.tasks[index]['description'] = description
            if status:
                self.tasks[index]['status'] = status
            self.save_tasks()
        else:
            print("Index invalid!")

    # Șterge un task
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
        else:
            print("Index invalid!")

# Funcția principală
def main():
    manager = TaskManager()

    while True:
        print("\n=== Task Manager ===")
        print("1. Adaugă task")
        print("2. Vezi task-uri")
        print("3. Editează task")
        print("4. Șterge task")
        print("5. Ieșire")
        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            title = input("Titlu: ")
            description = input("Descriere: ")
            task = Task(title, description)
            manager.add_task(task)
            print("Task adăugat cu succes!")
        elif optiune == "2":
            manager.view_tasks()
        elif optiune == "3":
            index = int(input("Index task de editat: ")) - 1
            title = input("Titlu nou (lasă gol pt. neschimbat): ")
            description = input("Descriere nouă (lasă gol pt. neschimbat): ")
            status = input("Status nou (Pending/In Progress/Completed): ")
            manager.edit_task(index, title or None, description or None, status or None)
        elif optiune == "4":
            index = int(input("Index task de șters: ")) - 1
            manager.delete_task(index)
            print("Task șters!")
        elif optiune == "5":
            print("Ieșire...")
            break
        else:
            print("Opțiune invalidă!")

if __name__ == "__main__":
    main()

