# ITL-Task

# 📝 Task Management System (Django + REST API)

This is a Task Management System built with **Django** and **Django REST Framework (DRF)**. It provides a powerful backend for managing tasks including **CRUD operations**, **user authentication**, **task filtering**, and more. You can integrate this backend with a frontend (like React) for a full-stack experience.

---

## 🚀 Features

- 🔐 Authenticated User Task Management
- ➕ Create Tasks
- 📋 List All Tasks (or only user-specific if logged in)
- ✏️ Update Tasks
- ❌ Delete Tasks
- 🔍 Task Detail View
- 🧠 REST API Powered
- 🔄 JSON-based request/response

---

## 📦 API Endpoints

| Method | Endpoint                 | Description                      | Authentication |
|--------|--------------------------|----------------------------------|----------------|
| GET    | `/api/tasks/`            | List all tasks (or user-specific)| Optional       |
| POST   | `/api/tasks/`            | Create new task                  | ✅ Required     |
| POST   | `/api/tasks/create/`     | Create task via serializer       | ✅ Required     |
| GET    | `/api/tasks/<id>/`       | Retrieve task details            | ❌ Optional     |
| PUT    | `/api/tasks/update/<id>/`| Update task                      | ✅ Required     |
| DELETE | `/api/tasks/delete/<id>/`| Delete task                      | ✅ Required     |

---

## 🛠️ Technologies Used

- **Python 3**
- **Django**
- **Django REST Framework**
- **SQLite (default) / PostgreSQL**
- **JSON APIs**

---

## 🧩 Models (Simplified)

```python
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
