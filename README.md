# End-to-End Jenkins AWS DevOps CI/CD

A hands-on DevOps project using:

- Linux and GitHub
- Docker and Docker Compose
- Jenkins CI/CD
- AWS and Amazon ECR
- Terraform
- Kubernetes
- Argo CD
- Prometheus and Grafana

## Application

Python Flask API running in a Docker container.

## Health Check

GET /health

## Run Locally

sudo docker compose up -d --build

curl http://127.0.0.1:5000/health
