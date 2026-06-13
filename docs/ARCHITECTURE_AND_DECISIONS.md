# Architecture and Decisions

## Project Overview
This project implements a production-oriented deployment platform for a simple FastAPI application backed by Redis.

## Initial Scope
The provided application includes:
- A FastAPI service
- A Redis dependency
- A basic Dockerfile

The assignment requires:
- CI/CD as the first implementation step
- Centralized log collection
- Performance testing and optimization
- Justification for all infrastructure decisions

## Decision 1: Restructuring the Repository
The repository was reorganized into separate domains:
- `app/` for application code
- `docker/` for image build instructions
- `deploy/` for deployment configuration
- `observability/` for logging components
- `performance/` for load testing
- `docs/` for architectural and operational documentation

### Justification
This separation improves maintainability, readability, and operational clarity.

## Decision 2: Dockerfile Optimization
The original Dockerfile was replaced with a multi-stage build using `python:3.9-slim`.

### Justification
- Reduced image size
- Better layer caching
- Lower attack surface
- Cleaner runtime image

## Decision 3: Non-root Container Execution
The application runs as a non-root user inside the container.

### Justification
This reduces the security impact of a container compromise.

## Decision 4: Health Endpoint
A `/health` endpoint was added.

### Justification
This supports:
- container health checks
- CI validation
- deployment verification
