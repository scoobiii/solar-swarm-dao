import os
import time
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def get_llm_analysis(project_name, tech_description):
    """Solicita análise ao DeepSeek local via Ollama"""
    endpoint = os.getenv("LLM_ENDPOINT", "http://localhost:11434/api/generate")
    prompt = (
        f"Analise o projeto '{project_name}' que usa a tecnologia '{tech_description}'. "
        "Escreva uma justificativa técnica curta (1 frase) em português explicando por que "
        "isso é importante para o Agentic Commerce. Termine com #USDCHackathon Vote"
    )
    
    try:
        response = requests.post(endpoint, json={
            "model": os.getenv("LLM_MODEL", "deepseek-r1:7b"),
            "prompt": prompt,
            "stream": False
        })
        return response.json().get('response', '').strip()
    except Exception as e:
        return f"Voto técnico para {project_name}. Inovação em {tech_description}. #USDCHackathon Vote"

def analyze_and_vote():
    AGENT_NAME = "SolarSwarm_Governance_Bot"
    print(f"🤖 {AGENT_NAME} iniciando análise via DeepSeek Local...")

    # Projetos reais ou simulados do Moltbook
    competitors = [
        {"name": "GreenDEX", "tech": "AMM for Carbon Credits"},
        {"name": "WaterAgent", "tech": "IoT Water Billing"},
        {"name": "YieldFarmer_AI", "tech": "Auto-compounding USDC"},
        {"name": "BaseCommerce", "tech": "P2P Retail Agents"},
        {"name": "ZeroWaste_DAO", "tech": "Recycling rewards in USDC"}
    ]

    for project in competitors:
        # O DeepSeek assume a lógica aqui:
        comment = get_llm_analysis(project['name'], project['tech'])
        
        print(f"📤 Analisando {project['name']}...")
        print(f"📝 Justificativa: {comment}")
        
        # Execução via CLI do OpenClaw (O Agente posta no Moltbook)
        # os.system(f'openclaw message send --message "{comment}"')
        
        time.sleep(1) # Rápido porque a LLM é local!

    print("🎉 Missão de governança concluída com DeepSeek-R1!")

if __name__ == "__main__":
    analyze_and_vote()
