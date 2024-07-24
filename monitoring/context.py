import monitoring.collectors_service as collectors_service
import monitoring_service
import alarm_service
import notifier_service
machines_location = './data/machines.csv'
metrics_location = './data/metrics.csv'
cpu_limit = 90
memory_threshold = 85
machines_collector = collectors_service.MachinesCollector(machines_location)
metrics_collector = collectors_service.MetricsCollector(metrics_location)

monitoring = monitoring_service.Monitoring()

alarm_manager = alarm_service.AlarmManager(cpu_limit, memory_threshold)

console_notifier = notifier_service.ConsoleNotifier()

alarm_manager.notifier = console_notifier
alarm_manager.monitoring = monitoring
alarm_manager.machines_collector = machines_collector

metrics_collector.machines_collector = machines_collector
monitoring.machines_collector = machines_collector
monitoring.metrics_collector = metrics_collector

