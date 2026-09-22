# 📘 Assignment: SQLite CRUD for Task Manager

## 🎯 Objective

Build a small task manager using Python and SQLite to practice database creation, data storage, andCRUD operations. This assignment helps students understand how real applications keep information persistent between runs.

## 📝 Tasks

### 🛠️ Set Up the Database

#### Descrição
Create a SQLite database and a table for storing tasks with a title, description, status, and creation date.

#### Requisitos
O programa concluído deve:

- Connect to a SQLite database with `sqlite3`.
- Create a `tasks` table with at least these fields: `id`, `title`, `description`, `completed`, and `created_at`.
- Use a proper schema so each task has a unique ID.
- Initialize the database automatically when the script starts.

### 🛠️ Create and Read Tasks

#### Descrição
Implement functions to insert new tasks and list all saved records.

#### Requisitos
O programa concluído deve:

- Add a function to insert a new task into the database.
- Add a function to retrieve all tasks from the table.
- Display tasks in a clear, readable format.
- Include at least one example task in the database for testing.

### 🛠️ Update and Delete Tasks

#### Descrição
Allow the user to change a task's status or remove it from the database.

#### Requisitos
O programa concluído deve:

- Add a function to mark a task as completed or incomplete.
- Add a function to delete a task by ID.
- Handle invalid task IDs gracefully.
- Confirm the result of each update or delete operation.

### 🛠️ Add a Simple Summary Report

#### Descrição
Create a summary feature that shows how many tasks are completed and how many are still pending.

#### Requisitos
O programa concluído deve:

- Count all tasks in the database.
- Count completed tasks separately.
- Count pending tasks separately.
- Print a small summary report in the terminal.
- Use the report to verify that the CRUD operations are working correctly.

## ✅ Completion Criteria

To complete the assignment, the student should be able to:

- create a SQLite database and schema;
- insert, read, update and delete records;
- use Python functions to manage persistent data;
- understand how CRUD operations are used in real applications.
