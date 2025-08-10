Iris Classification – End-to-End MLOps Pipeline
This repository contains a machine learning project for classifying the Iris flower species. It is built with a focus on MLOps principles, including CI/CD with GitHub Actions, containerization with Docker, experiment tracking, and monitoring.
This project implements an end-to-end MLOps pipeline for classifying the Iris dataset using logistic regression. It covers training, model tracking with MLflow, model selection & promotion, and deployment via a FastAPI endpoint.

✨ Features

    Automated CI/CD: The pipeline automatically tests and builds the project on every push to the main branch using GitHub Actions.

    Containerization: The application is containerized using Docker for consistent environments and easy deployment.

    Experiment Tracking: MLflow (mlruns directory) is used to log experiments, parameters, metrics, and models.

    API for Prediction: A Flask/FastAPI server exposes a prediction endpoint.

    Monitoring: Includes a prometheus.yml configuration for scraping metrics and monitoring the application.

    Code Quality: Follows a modular structure for better maintainability and scalability.

🌊 Project Workflow

    Code Push: A developer pushes code to the GitHub repository.

    CI Trigger: GitHub Actions triggers the CI/CD workflow defined in ci-cd.yml.

    Testing & Linting: The pipeline runs automated tests and lints the code.

    Build Docker Image: A Docker image is built based on the Dockerfile.

    Push to Registry: The newly built image is pushed to a container registry (like Docker Hub or GitHub Container Registry).

    Deployment: The image can then be pulled and deployed to a hosting environment (e.g., a cloud server).

    Monitoring: Prometheus scrapes metrics from the running application.

📂 Project Structure

Here is a breakdown of the key files and directories in this project:
<img width="845" height="663" alt="image" src="https://github.com/user-attachments/assets/d2f6411e-9105-47c0-a433-497fd235a9d2" />


🛠️ Technologies Used

    Language: Python

    Machine Learning: Scikit-learn, Pandas, NumPy

    API Framework: Flask / FastAPI

    CI/CD: GitHub Actions

    Containerization: Docker

    Experiment Tracking: MLflow

    Monitoring: Prometheus
