Operations Runbook

Purpose

This runbook provides the operational steps required to start, validate, observe, test, and stop the platform.

Components
The platform includes:

FastAPI application
Redis
Loki
Promtail
Start the Full Platform
docker compose -f deploy/docker-compose.yml up -d --build

Verify Platform Health
Application health:

curl http://localhost:8010/health

Expected response:

{“status”:“ok”}

Loki readiness:

curl http://localhost:3100/ready

Expected:

ready

Redis health:

docker exec -it redis_db redis-cli ping

Expected:

PONG

Functional Validation
Write test key:

curl -X POST “http://localhost:8010/write/test_key?value=passed”

Read test key:

curl “http://localhost:8010/read/test_key”

Viewing Logs
All services:

docker compose -f deploy/docker-compose.yml logs -f

Application logs:

docker compose -f deploy/docker-compose.yml logs -f app

Promtail logs:

docker compose -f deploy/docker-compose.yml logs -f promtail

Loki logs:

docker compose -f deploy/docker-compose.yml logs -f loki

Run Performance Test
docker run --rm -i -v $(pwd):/work --network host grafana/k6 run /work/performance/k6-test.js

Stop Platform
docker compose -f deploy/docker-compose.yml down

Rebuild Platform
docker compose -f deploy/docker-compose.yml up -d --build

CI Validation Stack
docker compose -f deploy/docker-compose.ci.yml up -d --build

docker compose -f deploy/docker-compose.ci.yml down

Notes
Loki and Promtail provide centralized logging.
Redis uses a Docker persistent volume.
Promtail may show old timestamps for existing containers; this is expected and harmless.
