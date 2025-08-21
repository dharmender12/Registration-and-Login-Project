# 📝 Registration and Login Project (Django)

This is a simple **Registration and Login system** built with **Django**.  
It allows users to **register, login, and logout**, with form validation and a success page after registration.

---

## ⚡ Features
- User registration with:
  - Username
  - Email
  - Password & confirm password
- Form validation (Django + jQuery)
- User authentication (login/logout)
- Success page after signup
- Responsive UI (based on Colorlib template)

---

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript (jQuery Validation)
- **Database:** SQLite (default Django DB)
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
Registration-and-Login-Project/
│── register_and_login/ # Main Django app
│ ├── templates/ # HTML templates (signup, login, success)
│ ├── static/ # CSS, JS, Images
│ ├── views.py # App views (register, login, success, logout)
│ ├── urls.py # App-level URLs
│── project_name/ # Django project settings
│── manage.py # Django project manager
│── README.md # Project documentation
```

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/dharmender12/Registration-and-Login-Project.git
   cd Registration-and-Login-Project


2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows
```
3. Install dependencies:
```bash
pip install django
```
4. Run migrations:
```
python manage.py migrate
```
5. Start the development server:
   ```
   python manage.py runserver

6. Open in browser:
```
http://127.0.0.1:8000/
```
📸 Screenshots
🔹 Registration Page

🔹 Login Page

🔹 Success Page



