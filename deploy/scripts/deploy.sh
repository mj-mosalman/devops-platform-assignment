#!/bin/bash
set -e

echo "Starting platform..."

docker compose -f deploy/docker-compose.yml up -d

echo "Deployment completed."
