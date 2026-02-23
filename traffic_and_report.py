import requests
import time

APP_URL = "http://localhost:5000/"
PROMETHEUS_API = "http://localhost:9090/api/v1/query"
QUERY = "app_orders_total"

def generate_traffic():
    for _ in range(50):
        requests.get(APP_URL)

def query_prometheus():
    response = requests.get(
        PROMETHEUS_API,
        params={"query": QUERY}
    )

    data = response.json()

    if data["status"] != "success":
        raise Exception("Prometheus query failed")

    result = data["data"]["result"]

    if not result:
        return 0

    value = result[0]["value"][1]
    return int(float(value))

def print_report(total_orders):
    print("===================================")
    print("SYSTEM METRICS REPORT")
    print("===================================")
    print("Target Application: Order Processor")
    print("Metric Queried: app_orders_total")
    print("Status: SUCCESS")
    print("")
    print(f"Total Orders Processed: {total_orders}")
    print("===================================")

if __name__ == "__main__":
    generate_traffic()
    time.sleep(10)
    total = query_prometheus()
    print_report(total)
