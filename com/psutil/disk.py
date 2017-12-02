import psutil
print psutil.disk_partitions()
print psutil.disk_usage('/home')
print psutil.disk_io_counters()
print psutil.disk_io_counters(perdisk=True)
