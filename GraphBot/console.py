import time

### Logging commands
def log(message: str) -> str:
  print(f"[{time.strftime("%H:%M:%S")}] [SYS] {message}")

def info(message: str) -> str:
  print(f"[{time.strftime("%H:%M:%S")}] [INFO] {message}")

def error(message: str) -> str:
  print(f"[{time.strftime("%H:%M:%S")}] [ERR] {message}")

def client(message: str) -> str:
  print(f"[{time.strftime("%H:%M:%S")}] [CLI] {message}")

### Timestamps
def timestamp() -> float:
  return time.time()