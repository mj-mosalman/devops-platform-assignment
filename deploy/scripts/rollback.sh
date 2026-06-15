#!/bin/bash
set -e

echo "Rolling back deployment..."

docker compose -f deploy/docker-compose.yml down
docker compose -f deploy/docker-compose.yml up -d

echo "Rollback completed."
