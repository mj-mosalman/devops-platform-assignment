Performance Test Report

Tool
Load testing was executed using k6.

Test Scenario
Virtual Users: 50
Test Duration: 30 seconds
Endpoints tested:
POST /write/{key}
GET /read/{key}
The test simulates concurrent clients performing write and read operations against the FastAPI service backed by Redis.

Execution Command
docker run --rm -i \

-v $(pwd):/work \

–network host \

grafana/k6 run /work/performance/k6-test.js

Results
Total requests: 2902
Requests per second: ~93 req/s
Failed requests: 0%
Latency metrics:

Average response time: 25.35 ms
Median response time: 8.47 ms
90th percentile: 60.3 ms
95th percentile: 131.87 ms
Maximum observed latency: 386 ms
Observations
The service handled 50 concurrent users without errors.
Response times remained low throughout the test.
Redis-backed read/write operations showed stable performance.
Conclusion
The platform successfully handled concurrent load with zero request failures and low latency, indicating that the current architecture (FastAPI + Redis + Docker deployment) performs reliably under moderate traffic.
