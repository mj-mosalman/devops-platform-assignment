1. Start the platform
docker compose -f deploy/docker-compose.yml up -d

2. Verify health
curl http://localhost:8010/health

3. Run performance test
docker run --rm -i -v $(pwd):/work --network host grafana/k6 run /work/performance/k6-test.js
