import os, subprocess

def clear_screen():
    os.system("cls")

def run_server():
    os.chdir(r".")
    subprocess.Popen(["start", "cmd", "/k", "py server.py"], shell=True)
    print("Servidor ejecutado correctamente.")

