# DevOps Platform Assignment

This repository contains a production-oriented DevOps assignment implementation for a FastAPI service backed by Redis.

## Included Deliverables
- Optimized Docker image
- Docker Compose deployment
- CI/CD pipeline
- Health checks
- Centralized logging with Loki and Promtail
- Performance testing with k6
- Architecture and decision documentation
- Operations runbook

## Project Structure
- `app/` - FastAPI application source code
- `docker/` - Docker build definition
- `deploy/` - deployment and Compose files
- `ci/` - CI validation scripts
- `observability/` - logging configuration
- `performance/` - k6 load test scripts
- `docs/` - architecture, operations, and performance documentation

## Quick Start
### Start the platform
```bash
docker compose -f deploy/docker-compose.yml up -d --build
