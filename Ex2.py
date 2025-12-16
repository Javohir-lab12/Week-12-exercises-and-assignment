log_data = """[INFO] System started successfully
[WARNING] Memory usage high
[ERROR] Database connection failed
[INFO] User logged in
[ERROR] Payment gateway timeout
[INFO] Scheduled backup complete
[ERROR] Disk space critical"""

with open("server_log.txt", "w") as f:
    f.write(log_data)
counter = 0
with open("server_log.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            counter += 1
            with open("urgent_alerts.txt" , "a") as result:
                result.write(f"{line}")
print(f"Scan complete. Found {counter} errors.\nPlease check urgent_alerts.txt.")