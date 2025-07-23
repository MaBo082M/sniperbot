import os
import time
from dotenv import load_dotenv

load_dotenv()

def sniper_loop():
    wallet = os.getenv("WALLET_ADDRESS")
    print(f"[SNIPER] Wallet aktiv: {wallet}")
    while True:
        print("[SNIPER] Suche nach Token-Launches...")
        time.sleep(5)

if __name__ == "__main__":
    sniper_loop()
