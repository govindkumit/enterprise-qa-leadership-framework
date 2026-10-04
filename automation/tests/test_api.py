import subprocess, sys, time, requests

def test_products_api():
    p = subprocess.Popen([sys.executable, "automation/app.py"])
    try:
        time.sleep(1)
        r = requests.get("http://127.0.0.1:8000/products", timeout=5)
        assert r.status_code == 200
        assert len(r.json()["products"]) == 2
    finally:
        p.terminate(); p.wait()
