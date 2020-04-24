import psutil
import platform
from datetime import datetime

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}" +  f" and Release: {uname.release}")
#print(f"Node Name: {uname.node}")
#print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}" + f" and Processor: {uname.processor}")

# Boot Time
#print("="*40, "Boot Time", "="*40)
#boot_time_timestamp = psutil.boot_time()
#bt = datetime.fromtimestamp(boot_time_timestamp)
#print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# let's print CPU information
print("="*40, "CPU Info", "="*40)
# number of cores
print("Physical cores:", str(psutil.cpu_count(logical=False)) + " and Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
#print("CPU Usage Per Core:")
#for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
#    print(f"Core {i}: {percentage}%")
print(psutil.virtual_memory())  # physical memory usage
print('System Memory % used:', psutil.virtual_memory()[2])
