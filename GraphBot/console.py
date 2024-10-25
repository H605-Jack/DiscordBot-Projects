import time

def log(message: str):
  return f"[{time.strftime("%H:%M:%S")}] [SYS] {message}"

def info(message: str):
  return f"[{time.strftime("%H:%M:%S")}] [INFO] {message}"

def error(message: str):
  return f"[{time.strftime("%H:%M:%S")}] [ERR] {message}"

def client(message: str):
  return f"[{time.strftime("%H:%M:%S")}] [CLI] {message}"

