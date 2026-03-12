# DevOps Intern Final Project

**Name:** Siddhant Dongre  
**Date:** 13th March 2026  

## Project Overview
This repository demonstrates a complete, small-scale DevOps workflow. It integrates Linux scripting, Docker containerization, continuous integration using GitHub Actions, job orchestration using HashiCorp Nomad, and log monitoring with Grafana Loki.

## Repository Structure
* `scripts/`: Contains Linux system administration scripts.
* `Dockerfile`: Containerization instructions for the Python application.
* `.github/workflows/`: CI/CD pipeline configuration.
* `nomad/`: Infrastructure as Code (IaC) for Nomad deployment.
* `monitoring/`: Documentation and setup instructions for Grafana Loki.
* `mlflow/`: Extra credit MLOps tracking setup.

## How to Run

1. **Run Python Script:** `python hello.py`
2. **Run System Info Script:** `./scripts/sysinfo.sh`
3. **Build Docker Image:** `docker build -t devops-hello .`
4. **Run Docker Container:** `docker run devops-hello`
5. **Run Nomad Job:** `nomad job run nomad/hello.nomad`