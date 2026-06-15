# Architecture and Decisions

## Project Overview
This project delivers a production-oriented deployment platform for a FastAPI service backed by Redis.

The assignment required:
- implementing CI/CD as the first step
- collecting logs from platform services
- conducting performance testing
- optimizing the Docker image and infrastructure
- documenting and justifying all implementation decisions

---

## Decision 1: CI/CD Was Treated as a First-Class Concern

The CI/CD pipeline was designed as an early implementation priority rather than being added at the end of the project.

### Justification
The assignment explicitly required CI/CD to be established first.  
For that reason, the delivery flow was designed so that every change can be validated automatically through container build, service startup, health verification, and integration testing.

This approach reduces the risk of late-stage integration failures and ensures that infrastructure and application changes remain testable throughout development.

---

## Decision 2: Repository Restructuring by Responsibility

The repository was reorganized into clear functional domains:
- `app/` for application source code and Python dependencies
- `docker/` for image build instructions
- `deploy/` for Docker Compose deployment definitions
- `observability/` for logging configuration
- `performance/` for load testing artifacts
- `docs/` for architecture, operations, and performance documentation

### Justification
Separating files by operational responsibility improves maintainability, readability, and change isolation.  
It also makes the project easier to review, test, and extend.

---

## Decision 3: Dockerfile Optimization with Multi-Stage Build

The original Dockerfile was replaced with a multi-stage build based on `python:3.9-slim`.

### Justification
This decision improves build efficiency and runtime security by:
- reducing final image size
- improving dependency layer caching
- removing unnecessary build tools from the runtime image
- reducing attack surface

The resulting image is more suitable for CI/CD and deployment environments than a single-stage, full Python base image.

---

## Decision 4: Running the Application as a Non-Root User

The application container runs as a dedicated non-root user.

### Justification
Running containers as non-root is a standard hardening measure.  
It limits the blast radius of a potential container compromise and aligns the deployment with safer container security practices.

---

## Decision 5: Health Endpoint and Service Health Validation

A `/health` endpoint was added and used for service validation.

### Justification
Health validation is required for reliable container orchestration and automated delivery.  
The endpoint is used to:
- verify application readiness
- support health checks
- enable CI validation after stack startup
- simplify operational troubleshooting

This creates a simple and deterministic way to confirm that the application is actually serving traffic.

---

## Decision 6: Integration-Focused CI Pipeline

The CI pipeline validates the platform by starting the required services with Docker Compose and performing end-to-end checks instead of only building the image.

### Justification
A container image build alone does not prove that the application can communicate with Redis or serve requests correctly.  
Using Docker Compose in CI ensures that service interaction is tested, not just syntax or packaging.

This improves fault tolerance in the delivery process and catches configuration or runtime issues earlier.

---

## Decision 7: Isolated CI Stack Using `docker-compose.ci.yml`

A dedicated Compose file was introduced for CI execution.

### Justification
CI should run only the minimum required components needed to validate the application.  
Excluding observability services from CI reduces:
- startup time
- resource usage
- execution complexity
- failure surface

This makes the pipeline faster and more deterministic while still validating the core application flow.

---

## Decision 8: Centralized Logging with Loki and Promtail

Loki and Promtail were selected for log collection and aggregation.

### Justification
The assignment required collecting logs from platform services.  
Loki was chosen because it provides a lightweight and operationally efficient logging stack compared to heavier alternatives such as ELK.

The main reasons for this choice are:
- lower infrastructure overhead
- simpler deployment for containerized environments
- good compatibility with Docker log collection
- native integration with Grafana-based observability workflows

This made Loki a pragmatic choice for the scale and scope of the assignment.

---

## Decision 9: Redis Persistence Through Docker Volumes

Redis was configured with persistent storage using a Docker volume.

### Justification
Without persistence, Redis data would be lost whenever the container is recreated.  
Using a named volume improves resilience and better reflects realistic platform behavior where service restarts should not automatically destroy state.

---

## Decision 10: Performance Testing with k6

k6 was used to execute HTTP load testing against the application endpoints.

### Justification
The assignment required performance testing of the implemented platform.  
k6 was selected because it is:
- lightweight
- easy to run in containers
- suitable for HTTP workloads
- commonly used in engineering and CI workflows

Its scripting model also makes the performance test reproducible and easy to document.

---

## Decision 11: Full Stack for Local Validation, Minimal Stack for CI

Two deployment modes were maintained:
- `deploy/docker-compose.yml` for full local or production-like validation
- `deploy/docker-compose.ci.yml` for fast CI execution

### Justification
Local validation and CI have different goals.  
The full stack is useful for validating infrastructure behavior, logging, and service interactions in a more realistic environment.  
The CI stack is intentionally smaller to keep automated validation fast and reliable.

This separation prevents overloading CI while preserving a richer local testing workflow.

---

## Decision 12: Documentation as Part of the Deliverable

Architecture notes, operational runbook, and performance test results were documented in Markdown files.

### Justification
The assignment explicitly requires decision traceability and justification.  
Documentation was treated as part of the deliverable rather than an optional afterthought so that reviewers can understand:
- what was implemented
- why it was implemented that way
- how to run and validate the platform
- what performance characteristics were observed
