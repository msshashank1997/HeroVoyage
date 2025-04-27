<p align="center">
  <img src="./.png" alt="Hero-Voyage Banner" width="600"/>
</p>

# 🚂 Hero-Voyage: Train Booking Platform

Welcome to **Hero-Voyage** — a seamless, real-time train booking system built using **Flask**, **MongoDB**, and **Docker**.  
Whether you're a **User**, **Admin**, or **Driver**, Hero-Voyage provides an intuitive interface for easy operations.

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-2.x-black?logo=flask" />
  <img src="https://img.shields.io/badge/MongoDB-6.x-green?logo=mongodb" />
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker" />
</p>

---

## ✨ Features

- 🔒 User Registration and Authentication
- 🛠️ Admin Panel for Transport Management
- 🚚 Driver Panel for Assigned Tasks
- 🎟️ Ticket Booking with Random Seat and Coach Assignment
- 📄 Receipt Generation after Booking
- 🛢️ MongoDB for Backend Storage
- 🐳 Docker and Docker Compose Support for Easy Deployment

---

## 🛠️ Prerequisites

- [Python 3.11+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [MongoDB](https://www.mongodb.com/)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd hero-voyage
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=mongodb://localhost:27017/hero_voyage
SECRET_KEY=your_secret_key_here
```

> 🔐 Replace `your_secret_key_here` with a strong key.

---

### 3. Upload Train Data

Populate your database:

```bash
python upload_train_data.py
```

> 🛤️ Modify `train_data.csv` as needed before uploading.

---

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the Application

```bash
python bookingapp.py
```

By default, the app is live at:

```
http://localhost:4000/
```

---

## 🐳 Run with Docker

### Build the Docker Image

```bash
docker build -t hero-voyage .
```

### Run the Docker Container

```bash
docker run -p 4000:4000 --env-file .env hero-voyage
```

---

## 🐳🚀 Run with Docker Compose

```yaml
# docker-compose.yml
version: '3'
services:
  hero-voyage:
    build: .
    ports:
      - "4000:4000"
    env_file:
      - .env
```

Run:

```bash
docker-compose up
```

---

## 🗂️ Project Structure

```
hero-voyage/
├── bookingapp.py
├── upload_train_data.py
├── train_data.csv
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── admin.html
│   ├── driver.html
│   ├── user.html
│   └── receipt.html
├── static/
│   └── styles.css
└── .env
```

---

## 🧪 Testing the App

- Register a new user `/register`
- Login `/login`
- Admin Panel `/admin`
- Driver Panel `/driver`
- Book tickets `/user`
- View Receipt `/receipt`

---

## ⚡ Troubleshooting

| Problem                    | Solution |
| --------------------------- | -------- |
| MongoDB connection error    | Ensure MongoDB service is running locally or remotely |
| Port conflict               | Change the port number in `bookingapp.py` |
| Docker issues               | Make sure Docker Engine is installed and running |

---

## 🤝 Contributing

We welcome contributions!  
Feel free to fork the repository, open issues, or submit pull requests.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  🚂 <b>All aboard!</b> Hero-Voyage is your ticket to seamless train bookings! 🚂
</p>
