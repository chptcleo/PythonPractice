import psutil
print psutil.pids()
p = psutil.Process(1200)
print p.name(), p.exe(), p.cwd(), p.status, p.create_time(), p.uids(), p.gids(), p.cpu_times(), p.cpu_affinity()
print p.memory_percent(), p.memory_info(), p.io_counters(), p.connections(), p.num_threads()
