# Overview

As a software engineer, my goal is to build practical applications that integrate with modern cloud technologies to enhance my skills and create scalable solutions. This project is a to-do list application that interacts with a Cloud Database, allowing users to create, read, update, and delete tasks, all stored remotely. The application demonstrates key concepts of cloud computing, data storage, and application development.

The software provides an intuitive user interface for managing tasks. Users can add new tasks, mark tasks as complete, and delete tasks. All data is stored in a Firebase Cloud Firestore database, making it accessible across devices.

You can view the software in action, see the cloud database in use, and get an explanation of the code in the demonstration video linked below.

[Software Demo Video](https://youtu.be/726MGVpFACY)

# Cloud Database

This application uses Firebase Firestore as the cloud database. Firestore is a flexible, scalable database for mobile, web, and server development. It stores data in collections and documents, with each document containing key-value pairs.

The Firestore database structure for this project includes:
- **Tasks Collection**: Each task is stored as a document in this collection. A task document contains the following fields:
  - `task_name`: A string representing the task description.
  - `completed`: A boolean indicating whether the task has been completed.
  - `timestamp`: A timestamp of when the task was created.

# Development Environment

To develop this software, I used the following tools and technologies:
- **Programming Language**: Python, for its simplicity and power in backend development.
- **Libraries**:
  - `firebase-admin`: A Python library for interacting with Firebase services like Firestore.
  - `python-dotenv`: For managing environment variables securely.

The development environment also includes Firebase for the cloud database and a local Python environment for running the application.

# Useful Websites

Here are some websites that were helpful during this project:

- [Firebase Documentation](https://firebase.google.com/docs/firestore/quickstart?hl=pt-br#python)
- [Google Authentication](https://cloud.google.com/docs/authentication/getting-started)

# Future Work

The following improvements and additions are planned for future updates:

- Add user authentication (e.g., via Firebase Authentication).
- Implement sorting and filtering options for tasks.
- Add notifications for upcoming or overdue tasks.
- Improve the user interface with better design and UX features.
- Expand the application to support multiple users with distinct task lists.
