# DevPulse: CI/CD Monitoring Dashboard

Simulated CI/CD performance metrics visualized with Prometheus and Grafana.

## Features
- Simulates deployment, test pass/fail, and recovery metrics.
- Prometheus scrapes the metrics.
- Grafana dashboard for visualization.

## Setup

### Requirements
- Docker
- Docker Compose

### Run
```bash
docker-compose up --build
```

Visit:
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (Login: admin / admin)
