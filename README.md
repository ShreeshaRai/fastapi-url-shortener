#  FastAPI URL Shortener

A simple and efficient URL Shortener API built using **FastAPI**, **SQLAlchemy**, and **SQLite**.

This project allows users to convert long URLs into short, shareable links and automatically redirects users to the original URL.

---

##  Features

- Shorten long URLs
- Automatic redirection
- Base62 encoding for short links
- SQLite database integration
- Clean REST API design
- Interactive API documentation using Swagger UI

---

## 🛠️ Tech Stack

- Python 3.14
- FastAPI
- SQLAlchemy ORM
- SQLite
- Uvicorn
- Swagger UI

---

##  Project Structure

```
fastapi-url-shortener/
│── main.py
│── models.py
│── database.py
│── utils.py
│── .gitignore
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️ Clone the repository

```
git clone https://github.com/ShreeshaRai/fastapi-url-shortener.git
cd fastapi-url-shortener
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate it:

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

### 3️⃣ Install dependencies

```
pip install fastapi uvicorn sqlalchemy
```

### 4️⃣ Run the server

```
uvicorn main:app --reload
```

Server runs at:
```
http://127.0.0.1:8000
```

Swagger Documentation:
```
http://127.0.0.1:8000/docs
```

---

##  API Endpoints

###  Shorten URL

```
POST /shorten
```

###  Redirect

```
GET /r/{short_code}
```

---

##  Future Improvements

- Custom alias support
- Click tracking analytics
- Expiration time for links
- Deployment to cloud (Render/Railway)
- PostgreSQL integration

---

##  Author

**Shreesha Rai**  
Computer Science Engineer  
Aspiring AI/ML Engineer  

GitHub: https://github.com/ShreeshaRai
