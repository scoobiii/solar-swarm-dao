import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

class SolarSkill:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(os.getenv("BASE_SEPOLIA_RPC")))
        self.account = self.w3.eth.account.from_key(os.getenv("AGENT_PRIVATE_KEY"))
        self.contract_address = os.getenv("ESCROW_ADDRESS")
        # ABI simplificada para as funções core
        self.abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"_kwh","type":"uint256"},{"internalType":"uint256","name":"_price","type":"uint256"}],"name":"createOffer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"purchase","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.abi)

    def create_energy_offer(self, kwh_float, price_usdc_float):
        # Conversão para o padrão do Inquisidor (deci-kWh e 6 decimals)
        kwh_decis = int(kwh_float * 10)
        price_atomic = int(price_usdc_float * 10**6)
        
        tx = self.contract.functions.createOffer(kwh_decis, price_atomic).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 200000,
            'gasPrice': self.w3.eth.gas_price
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.w3.to_hex(tx_hash)

    def get_surplus(self):
        # Mock de integração com hardware (Simulação de 15.5 kWh)
        return 15.5
