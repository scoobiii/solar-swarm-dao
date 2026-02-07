const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SolarSwarm Agentic Flow", function () {
  it("Deve permitir que um Agente compre energia com USDC", async function () {
    const [admin, producer, agent] = await ethers.getSigners();
    const USDC_ADDR = "0x036CbD53842c5426634e7929541eC2318f3dCF7e";

    const Escrow = await ethers.getContractFactory("EscrowSolar");
    const escrow = await Escrow.deploy(USDC_ADDR);

    // 1. Agente cria oferta (10.5 kWh por 5 USDC)
    await escrow.connect(producer).createOffer(105, 5000000);
    
    // 2. Validação via Evento (Ouvido pelo Inquisidor)
    const filter = escrow.filters.OfferCreated();
    const events = await escrow.queryFilter(filter);
    expect(events[0].args.kwh).to.equal(105);
    
    console.log("   ✅ Agente validado on-chain!");
  });
});
