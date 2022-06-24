import shutil
import psutil

def check_disk_usage(path):
    global free_percentage
    free = shutil.disk_usage(path).free
    total = shutil.disk_usage(path).total
    free_percentage = (free/total)*100
    return free_percentage > 20

def check_cpu_usage():
    global cpu
    cpu = psutil.cpu_percent(0.1)
    return cpu < 75

if check_cpu_usage() and check_disk_usage("/"):
    print(f"Your machine is working fine \n  cpu:\t\t{cpu}\n  free disk:\t{free_percentage}")
else:
    print("your machine is performing abnormally")
