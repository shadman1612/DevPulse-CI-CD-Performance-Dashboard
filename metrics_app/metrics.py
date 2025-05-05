from prometheus_client import start_http_server, Summary, Counter, Gauge
import random, time

deployments = Counter("deployments_total", "Total deployments")
test_pass_rate = Gauge("test_pass_rate", "Test pass percentage")
recovery_time = Gauge("recovery_time_seconds", "Time to recover from failure")

if __name__ == "__main__":
    start_http_server(8000)
    while True:
        deployments.inc()
        test_pass_rate.set(random.uniform(80, 100))
        recovery_time.set(random.uniform(10, 60))
        time.sleep(5)
