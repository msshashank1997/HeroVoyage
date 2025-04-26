
# Hero-Voyage: Train Booking Application

Hero-Voyage is a Flask-based train booking application that allows users to register, log in, and book train tickets. It also includes admin and driver panels for managing transports and assigned tasks.

---

## Features
- **User Registration and Login**
- **Admin Panel** for managing transports
- **Driver Panel** for viewing assigned transports
- **Ticket Booking** with random seat and coach assignment
- **Receipt generation** for booked tickets
- **MongoDB integration** for data storage
- **Docker support** for containerized deployment

---

## Getting Started

### Prerequisites
- **Install Python**:  
  Download and install Python 3.11 or later from [python.org](https://www.python.org/).
- **Install Docker**:  
  Download and install Docker from [docker.com](https://www.docker.com/).
- **Install MongoDB**:  
  Install MongoDB locally or use a cloud-hosted MongoDB instance (e.g., [MongoDB Atlas](https://www.mongodb.com/atlas)).

---

## Steps to Run the Application

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd hero-voyage
```

### 2. Set Up Environment Variables
Create a `.env` file in the project directory with the following content:

```env
MONGO_URI=mongodb://localhost:27017/hero_voyage
SECRET_KEY=your_secret_key
```
> Replace `mongodb://localhost:27017/hero_voyage` with your MongoDB URI if using a remote database.  
> Replace `your_secret_key` with a secure key for session management.

### 3. Install Dependencies
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask application:

```bash
python bookingapp.py
```

### 5. Access the Application
Open your browser and navigate to:

```
http://localhost:4000/
```

---

## Using Docker

### Dockerfile Explanation

The Dockerfile is used to containerize the application. Here's a breakdown of its contents:

**Key Points:**
- **Base Image**:  
  Uses the official Python 3.11 slim image for a lightweight container.
- **Working Directory**:  
  Sets `/app` as the working directory inside the container.
- **Dependencies**:  
  Installs all dependencies listed in `requirements.txt`.
- **Port Exposure**:  
  Exposes port `4000` for the Flask application.
- **Environment Variables**:  
  Configures Flask to run on `0.0.0.0` (accessible from outside the container).
- **Command**:  
  Runs the Flask application using `flask run`.

---

### Steps to Run with Docker

#### 1. Build the Docker Image
```bash
docker build -t hero-voyage .
```

#### 2. Run the Docker Container
```bash
docker run -p 4000:4000 --env-file .env hero-voyage
```

#### 3. Access the Application
Open your browser and navigate to:

```
http://localhost:4000/
```

---

## Using Docker Compose (Optional)

If you want to simplify the process, you can use Docker Compose.

Create a `docker-compose.yml` file with the following content:

```yaml
version: '3'
services:
  hero-voyage:
    build: .
    ports:
      - "4000:4000"
    env_file:
      - .env
```

Run the application using:

```bash
docker-compose up
```

---

## Project Structure
```
hero-voyage/
├── bookingapp.py
├── Dockerfile
├── docker-compose.yml (optional)
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

## Testing the Application

### Register a User
- Go to `/register` and create a user with the role: `user`, `admin`, or `driver`.

### Log In
- Log in with the registered credentials.

### Admin Panel
- Log in as an **admin** to access the `/admin` panel and manage transports.

### Driver Panel
- Log in as a **driver** to view assigned transports.

### Book Tickets
- Log in as a **user** to book tickets and view receipts.

---

## Troubleshooting

- **MongoDB Connection Issues**:  
  Ensure MongoDB is running and the `MONGO_URI` in `.env` is correct.

- **Port Conflicts**:  
  If port `4000` is in use, change it in `bookingapp.py` or the `Dockerfile`.

- **Docker Issues**:  
  Ensure Docker is installed and running. Use `docker ps` to check running containers.

---

## Contributing
Feel free to fork this repository and submit pull requests for improvements or bug fixes.

---

## License
This project is licensed under the [MIT License](LICENSE).



---

Would you also like me to generate a ready-to-use `.md` file and send it to you directly? 🚀  
(so you can just download it and use it!)
