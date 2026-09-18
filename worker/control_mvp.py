import json,math,pathlib
# Plant G(s)=1/(tau*s+1), proportional controller Kp.
tau=2.0; Kp=3.0
closed_loop_gain=Kp/(1.0+Kp)
closed_loop_tau=tau/(1.0+Kp)
pole=-1.0/closed_loop_tau
passed=math.isclose(closed_loop_gain,0.75,rel_tol=1e-12) and math.isclose(closed_loop_tau,0.5,rel_tol=1e-12) and pole<0
out={"benchmark":"first_order_proportional_closed_loop","engine":"PY-CONTROL-MVP","closed_loop_gain":closed_loop_gain,"closed_loop_tau_s":closed_loop_tau,"pole":pole,"stable_model":pole<0,"passed":passed,"evidence_level":"E2","limitations":["analytical model benchmark","not SIL integration","not HIL","not physical test"]}
pathlib.Path("artifacts").mkdir(exist_ok=True); pathlib.Path("artifacts/control_mvp.json").write_text(json.dumps(out,indent=2),encoding="utf-8"); print(json.dumps(out,indent=2)); raise SystemExit(0 if passed else 1)
