**Order Processor – DevOps Demo**
This project demonstrates production-style DevOps practices applied to a simple Flask application.
It includes:
Containerized Python application
Prometheus metrics instrumentation
Grafana visualization
Docker Compose infrastructure
Automated traffic generation and metric reporting
GitHub Actions CI pipeline
Trivy vulnerability scanning with build failure guardrail

**Architecture**
User Request → Flask App → Prometheus → Grafana
CI Pipeline → Docker Build → Trivy Scan → Fail on Critical Issues

**Services**
Service	URL
App	http://localhost:5000
Prometheus	http://localhost:9090

Grafana	http://localhost:3000

**Grafana default credentials:**
admin / admin

Run the Stack
docker-compose up --build
Metric
The application exposes a custom Prometheus counter:
app_orders_total
Every request to / increments this metric.

**Metrics endpoint:**
http://localhost:8000/metrics

**Grafana Setup**
Add Prometheus as a data source
URL: http://prometheus:9090
Create a dashboard panel using:
app_orders_total
Automated Traffic & Reporting

**Run:**
**python traffic_and_report.py**
**The script:**
Sends 50 requests to the app
Waits for Prometheus scrape
Queries Prometheus API
Parses JSON response
Prints a formatted metrics report
CI & Security
Workflow: .github/workflows/ci.yml
On every push:
Build Docker image (tagged with commit SHA)
Scan image using Trivy
Fail pipeline if CRITICAL vulnerabilities are found
Security guardrail validated by intentionally using an outdated base image and confirming pipeline failure.

**Why This Project?**
Demonstrates practical DevOps fundamentals:
Observability
Infrastructure as Code
Automated metric reporting
CI automation
Image security enforcement
