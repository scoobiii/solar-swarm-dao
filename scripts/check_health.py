from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

def check_agent_vitals():
    w3 = Web3(Web3.HTTPProvider(os.getenv("BASE_SEPOLIA_RPC")))
    agent_addr = os.getenv("AGENT_ADDRESS")
    
    eth_balance = w3.eth.get_balance(agent_addr)
    print(f"💰 Saldo Gas (ETH): {w3.from_hex(eth_balance)} ETH")
    
    if eth_balance == 0:
        print("⚠️ ALERTA: Agente sem combustível para transações!")
    else:
        print("✅ Agente pronto para o combate.")

if __name__ == "__main__":
    check_agent_vitals()
