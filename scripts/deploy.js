const hre = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log(`🚀 Deploying com a conta: ${deployer.address}`);

  const USDC_BASE_SEPOLIA = "0x036CbD53842c5426634e7929541eC2318f3dCF7e";
  
  const Escrow = await hre.ethers.getContractFactory("EscrowSolar");
  const escrow = await Escrow.deploy(USDC_BASE_SEPOLIA);

  await escrow.waitForDeployment();
  const address = await escrow.getAddress();

  console.log(`✅ EscrowSolar deployado em: ${address}`);
  console.log(`💡 Copie este endereço para o seu .env em ESCROW_ADDRESS`);
}

main().catch((error) => { console.error(error); process.exitCode = 1; });
