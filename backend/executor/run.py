import sys
import io
import contextlib
import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

code = sys.stdin.read()

output = io.StringIO()

with contextlib.redirect_stdout(output):
    with contextlib.redirect_stderr(output):
        try:
            exec(code, {})
        except Exception as e:
            print("Error:", e)

image_data = ""

figs = plt.get_fignums()
if figs:
    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=100)
    buf.seek(0)
    image_data = base64.b64encode(buf.read()).decode("utf-8")
    plt.close("all")

print("<<OUTPUT>>" + output.getvalue().replace("\n", "\\n"))
print("<<IMAGE>>" + image_data)
