# 🎯 CareerCompass – Job Application Tracker

**CareerCompass** is a full-stack web app built with Django that helps users track their job applications, monitor progress, and visualize insights with an interactive dashboard.

---

## 🚀 Features

- 📝 **Add / Edit / Delete Applications**
- 📊 **Dashboard** showing totals and charts by status
- 🔒 **User Authentication**
- 🎨 **Clean Tailwind-style UI**
- ☁️ **Ready for Render Deployment**

---

## 🛠️ Tech Stack

| Layer | Framework / Tool |
|-------|------------------|
| Backend | Django 5 + Gunicorn |
| Frontend | HTML + TailwindCSS |
| Database | SQLite (local) / PostgreSQL (Render) |
| Hosting | Render Free Web Service |
| Analytics | Chart.js |

---

## ⚙️ Local Setup

```bash
git clone https://github.com/<your-username>/careercompass.git
cd careercompass
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

