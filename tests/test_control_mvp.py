import subprocess,sys,json,pathlib
r=subprocess.run([sys.executable,"worker/control_mvp.py"],check=False); assert r.returncode==0
x=json.loads(pathlib.Path("artifacts/control_mvp.json").read_text()); assert x["passed"] is True and x["stable_model"] is True
