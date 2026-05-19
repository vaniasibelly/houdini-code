import os
import time
import sys

def fork_bomb():
    MAX_ATTEMPTS = 20
    attempts = 0
    blocked = 0
    
    while attempts < MAX_ATTEMPTS:
        try:
            os.fork()
            attempts += 1
        except OSError as e:
            blocked += 1
            print(f"Fork failed (attempt {attempts + blocked}): {e}")
            sys.stdout.flush()  # Flush the output buffer immediately
            attempts += 1

    print(f"\n--- Resultado ---")
    print(f"Tentativas de fork: {attempts + blocked}")
    print(f"Forks bloqueados pelo cgroup: {blocked}")
    if blocked > 0:
        print("✅ pids_limit funcionou: o cgroup bloqueou o fork bomb com sucesso!")
    else:
        print("❌ pids_limit nao funcionou: nenhum fork foi bloqueado.")

if __name__ == "__main__":
    print(f"Iniciando fork bomb com pids_limit=10...")
    print(f"PID atual: {os.getpid()}")
    fork_bomb()
    time.sleep(1)
