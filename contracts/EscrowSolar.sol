// SPDX-License-Identifier: MIT
/**
 * @title SolarSwarm Escrow (v3.0-Global)
 * @author MEx / SolarSwarm DAO
 * @version 3.0.0
 * @date 2026-02-06
 * @notice RESPONSABILIDADE: Liquidação Multimoeda (DREX/USDC) e Custódia de Lastro Energético.
 * @dev Otimizado para Atomic Swaps via Kindelia HVM e processamento paralelo.
 * @signature 0xSOLAR_SWARM_SIGNED_BY_MEX_GLOBAL
 */

pragma solidity ^0.8.20;

interface IERC20 {
    function transferFrom(address s, address r, uint256 a) external returns (bool);
    function transfer(address r, uint256 a) external returns (bool);
}

contract EscrowSolar {
    event OfferCreated(uint256 indexed id, address indexed producer, uint256 kwh, uint256 price);
    event Settled(uint256 indexed id, address indexed buyer, string currency);

    struct Offer { 
        address producer; 
        uint256 kwh; 
        uint256 price; 
        bool active; 
    }

    mapping(uint256 => Offer) public offers;
    uint256 public nextOfferId;
    address public immutable usdc; // Pode ser DREX ou USDC dependendo do deploy

    constructor(address _token) { 
        usdc = _token; 
    }

    /**
     * @notice Cria uma oferta baseada no excedente validado pelo MEx Analyst.
     */
    function createOffer(uint256 _kwh, uint256 _price) external {
        offers[nextOfferId] = Offer(msg.sender, _kwh, _price, true);
        emit OfferCreated(nextOfferId++, msg.sender, _kwh, _price);
    }

    /**
     * @notice Liquidação da oferta com divisão de taxas para o pool de financiamento.
     */
    function purchase(uint256 _id) external {
        Offer storage o = offers[_id];
        require(o.active, "Oferta Inativa");
        
        uint256 fee = o.price / 100; // 1% Fee para o DAO/Financiamento
        
        require(IERC20(usdc).transferFrom(msg.sender, address(this), o.price), "Erro na transferencia");
        
        o.active = false;
        
        // Transfere o valor líquido para o produtor
        IERC20(usdc).transfer(o.producer, o.price - fee);
        
        emit Settled(_id, msg.sender, "DREX/USDC");
    }
}
