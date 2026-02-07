#!/bin/bash
# Gerador de Ambiente Seguro SolarSwarm

if [ ! -f .env ]; then
  echo "🚀 Criando .env seguro..."
  echo "AGENT_PRIVATE_KEY=$(openssl rand -hex 32)" >> .env
  echo "BASE_SEPOLIA_RPC=https://sepolia.base.org" >> .env
  echo "USDC_ADDRESS=0x036CbD53842c5426634e7929541eC2318f3dCF7e" >> .env
  echo "ESCROW_ADDRESS=pending" >> .env
  chmod 600 .env
  echo "✅ .env criado com permissões restritas."
else
  echo "⚠️ .env já existe. Proteja suas chaves!"
fi
