# CareerCompass – Job Application Tracker

**Live Demo:**  
[Visit the live app → CareerCompass](https://careercompass-yi6c.onrender.com/apps)

---

## Project Overview

CareerCompass is a full-stack web application built with Django and TailwindCSS, designed to help users track their job applications through all stages — from applying to interviewing, offers, or rejection — and visualize trends via a dashboard.

---

## Features

| Feature | Description |
|----------|-------------|
| Add / Edit / Delete Applications | Manage job applications with company, role, status, notes, etc. |
| Dashboard with Charts | Visualize application distribution by status using Chart.js |
| Demo Login | Testable access via demo user (no setup required) |
| User Authentication | Secure login using Django’s built-in system |
| Responsive UI | Clean, mobile-friendly design with TailwindCSS |
| Deploy-Ready | Hosted on Render with static file handling via WhiteNoise |

---

## Demo Login

Use these credentials to test the app:

**Username:** demo  
**Password:** password  

You’ll gain access to all CRUD and dashboard functionality.

---

## Tech Stack

- **Backend:** Django 5  
- **Frontend / Styling:** HTML + TailwindCSS  
- **Charts / Analytics:** Chart.js  
- **Database (local):** SQLite  
- **Database (production):** SQLite (configurable to Postgres)  
- **Web Server:** Gunicorn + WhiteNoise  
- **Hosting / Deployment:** Render  

---

## Setup / Local Development

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/CareerCompass.git
   cd CareerCompass
