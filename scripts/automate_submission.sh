#!/bin/bash
# Submissão Automática SolarSwarm
WORKSPACE_PATH="$HOME/.openclaw/workspace/skills/solar-surplus-negotiator"

echo "📦 Empacotando Skill para o OpenClaw..."
mkdir -p "$WORKSPACE_PATH"
cp ./skills/solar-surplus-negotiator/SKILL.md "$WORKSPACE_PATH/"
cp ./skills/solar-surplus-negotiator/skill.py "$WORKSPACE_PATH/"

echo "🧪 Rodando Inquisidor antes do Push..."
npx hardhat test && echo "✅ DNA Aprovado!" || exit 1

echo "🚀 Abrindo PR no OpenClaw Upstream..."
gh pr create --title "feat: SolarSwarm DAO Agentic Energy" --body "Submissão para o #USDCHackathon"
