import collectors
import monitoring_service

machines_location = './data/machines.csv'
metrics_location = './data/metrics.csv'

machines_collector = collectors.MachinesCollector(machines_location)
metrics_collector = collectors.MetricsCollector(metrics_location)

monitoring = monitoring_service.Monitoring()

metrics_collector.machines_collector = machines_collector
monitoring.machines_collector = machines_collector
monitoring.metrics_collector = metrics_collector

