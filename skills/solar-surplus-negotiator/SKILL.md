# Skill: Solar Surplus Negotiator ☀️
**Role:** Energy Market Maker for SolarSwarm DAO.
**Model Requirement:** Claude Opus 4.6 or DeepSeek-R1 (Reasoning).

## Description
This skill enables an agent to monitor energy surplus, calculate fair market prices in USDC, and execute on-chain escrow transactions on Base Sepolia.

## Tools
- `get_surplus()`: Connects to local inverter/meter to check available kWh.
- `create_energy_offer(kwh, price_usdc)`: Lists energy for sale in the Escrow contract.
- `buy_energy(offer_id, total_usdc)`: Purchases available energy from another peer.
- `get_market_price()`: Analyzes recent successful transactions in the DAO to suggest price.

## Constraints
- All prices must be in 6-decimal USDC.
- Energy units must be in deci-kWh (e.g., 10.5 kWh = 105).
- Never execute a transaction without checking gas balance.
