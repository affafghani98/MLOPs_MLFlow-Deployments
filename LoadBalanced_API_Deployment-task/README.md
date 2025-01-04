# Task 2: Load Balanced ML API Deployment

This folder contains the implementation of Task , which demonstrates deploying a load-balanced machine learning API using Docker, Flask, and Nginx.

## **Overview**
- Two API instances are deployed to serve predictions.
- Requests are distributed evenly between the instances using an Nginx load balancer.
- Each API instance returns a unique identifier to indicate which instance handled the request.

---

## **Files**
- **`app.py`**: Flask-based API script for serving predictions.
- **`Dockerfile`**: Dockerfile for containerizing the Flask API.
- **`docker-compose.yml`**: Docker Compose file to orchestrate Nginx and the API containers.
- **`default.conf`**: Nginx configuration file for load balancing.
- **`requirements.txt`**: Python dependencies for the Flask API.

---

## **How to Run**

### **1. Prerequisites**
- Install **Docker** and **Docker Compose**.

### **2. Clone the Repository**
```bash
git clone <repo-url>
cd LoadBalanced_API_Deployment-task
```

### 3. Build and Start the Containers
```bash
docker-compose up --build

```

- This command will:

-Build the Flask API image from the Dockerfile.
-Start two API instances (ml-api-instance-1 and ml-api-instance-2).
-Start an Nginx container to load balance between the API instances.

### 4.  Test the Load Balancer
- You can test the deployment using curl:
 ```bash
   curl -X GET http://localhost/

```

### 5.  Expected Response
-Example response from one of the API instances:
```bash
{
    "message": "Prediction made",
    "instance_id": "172.18.0.2"
}
```

---

### **NOTES**
- The docker-compose.yml file defines the services:
  - Two Flask API instances (ml-api-instance-1 and ml-api-instance-2).
  - One Nginx container as the load balancer.
- Ensure ports 80, 5001, and 5002 are free before running the application.

---

  


