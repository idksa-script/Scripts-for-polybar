import psutil
import time

def get_cpu():
    while True:
        obtener_porcentaje = psutil.cpu_percent(interval=1)
        print(f"CPU: {obtener_porcentaje:.1f}%", flush=True)
        time.sleep(1)

if __name__ == "__main__":
    get_cpu()
