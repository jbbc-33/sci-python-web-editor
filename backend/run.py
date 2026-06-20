import sys
import matplotlib.pyplot as plt

code = sys.stdin.read()

# Espacio seguro de ejecución
local_env = {}

try:
    exec(code, {"plt": plt}, local_env)

    # Si se generó una figura, guardarla
    if plt.get_fignums():
        plt.savefig("output.png")
        plt.close()
except Exception as e:
    print(str(e))
