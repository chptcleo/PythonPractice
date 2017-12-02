import psutil
mem = psutil.virtual_memory()
print mem
print mem.total
print psutil.swap_memory()
