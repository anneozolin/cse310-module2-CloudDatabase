from firebase_config import db
from auth import sign_up, log_in, get_user_id
from tabulate import tabulate
import datetime
import getpass

# Global variable to store logged-in user
current_user = None

# Function to add a new task
def add_task(user_id, title, description, due_date):
    task_ref = db.collection("tasks").document(user_id).collection("user_tasks").document()
    task_ref.set({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.datetime.utcnow()
    })
    print("Task added successfully!")

# Function to retrieve and display tasks for the logged-in user
def get_tasks(user_id):
    tasks = db.collection("tasks").document(user_id).collection("user_tasks").stream()
    task_list = []
    for task in tasks:
        data = task.to_dict()
        task_list.append([
            task.id,
            data.get("title"),
            data.get("description"),
            data.get("due_date"),
            "Yes" if data.get("completed") else "No",
            data.get("created_at").strftime("%Y-%m-%d %H:%M:%S")
        ])
    
    if task_list:
        print(tabulate(task_list, headers=["ID", "Title", "Description", "Due Date", "Completed", "Created At"], tablefmt="grid"))
    else:
        print("No tasks found.")

# Function to update a task
def update_task(user_id, task_id, field, value):
    task_ref = db.collection("tasks").document(user_id).collection("user_tasks").document(task_id)
    task_ref.update({field: value})
    print("Task updated successfully!")

# Function to delete a task
def delete_task(user_id, task_id):
    db.collection("tasks").document(user_id).collection("user_tasks").document(task_id).delete()
    print("Task deleted successfully!")

# Main menu
def main():
    global current_user
    print("Welcome to the To-Do List App with Authentication")
    
    # User authentication
    while not current_user:
        print("\n1. Sign Up")
        print("2. Log In")
        choice = input("Choose an option: ")
        
        email = input("Email: ")
        password = getpass.getpass("Password: ")  # Hides password input
        
        if choice == "1":
            current_user = sign_up(email, password)
        elif choice == "2":
            current_user = log_in(email, password)
        else:
            print("Invalid choice. Please try again.")
    
    user_id = get_user_id(current_user)
    
    # To-Do List functionality
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Task Title: ")
            description = input("Task Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            add_task(user_id, title, description, due_date)
        
        elif choice == "2":
            get_tasks(user_id)
        
        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            field = input("Field to update (title, description, due_date, completed): ")
            value = input("New value: ")
            if field == "completed":
                value = value.lower() == 'true'
            update_task(user_id, task_id, field, value)
        
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            delete_task(user_id, task_id)
        
        elif choice == "5":
            print("Logging out...")
            current_user = None
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
