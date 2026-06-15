# DevOps Platform Assignment

This repository contains the implementation of a production-oriented platform for a FastAPI + Redis application.

## Goals
- Optimize the Docker image
- Implement CI/CD pipeline
- Centralize logs
- Run performance tests
- Document all architecture decisions

## Repository Structure
- `app/`: FastAPI application code
- `docker/`: Docker build instructions
- `deploy/`: deployment manifests and scripts
- `observability/`: logging stack configuration
- `performance/`: load test scripts
- `docs/`: technical documentation

## Quick Start

Start the platform:

docker compose -f deploy/docker-compose.yml up -d

Check health:

curl http://localhost:8010/health

Run performance test:

docker run --rm -i -v $(pwd):/work --network host grafana/k6 run /work/performance/k6-test.js
