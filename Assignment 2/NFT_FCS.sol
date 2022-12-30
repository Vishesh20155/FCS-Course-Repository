// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

// The following libraries have an implementation of ERC721 standard of NFT. 
// Implementation of necessary functions as mentioned here: https://eips.ethereum.org/EIPS/eip-721 
// is done in these imported libraries.
// The code in these libraries ensure security and correctness of the impementation as it is globally accepted 
import "https://github.com/0xcert/ethereum-erc721/src/contracts/tokens/nf-token-metadata.sol";
import "https://github.com/0xcert/ethereum-erc721/src/contracts/ownership/ownable.sol";

// The implementation of the following mentioned functions in the documentation is defined:
// balanceOf -> no of NFTs assigned to an owner 
// ownerOf -> return the owner of an NFT
// safeTransferFrom -> Transfers ownership of an NFT from one address to another
// safeTransferFrom -> transfers ownership of an NFT
// approve -> to approve the address of NFT
// setApprovalForAll -> to enable third party's management
// getApproved -> to get the approved address of an NFT
// isApprovedForAll -> to check if an address is authorised operator for another address
 

// The contract inherits NFTokenMetaData and Ownable from the above imported libraries.
// This is the actual implementation of ERC721 Standard of token and consists of the implementation of the above mentioned functions.
contract FCS_A2_Q4 is NFTokenMetadata, Ownable {
 
    uint256 mintedNFT; // This variable is used to check the number of NFTs minted. It's upper limit is set to 1000 so that there is not infinite minting.
    
    // The constructor is used to initialize the name and the symbol of the NFT contract.
    constructor() {
        nftName = "NFT FCS A2 Q4"; // Variable to initialize the NFT Contract name.
        nftSymbol = "FCS"; // Variable to initialize NFT contract symbol
    }

    // Below is the actual function that implements the functionality of minting the NFTs. It uses the '_mint()' functionality of the super classes that have been inherited.
    // The parameter '_to' is of address type and determines the wallet address of the person for whom the NFT will be minted.
    // The parameter '_tokenId' is used to specify the token ID of the NFT. An NFT is uniquely identified by the pair (contract_address, token_id)
    // The parameter URI is the hash of the file that needs to be uploaded on ipfs as NFT. It consists of the link of the image, its name and its description, that may be identified from the JSON file
    // 'onlyOwner' means that only the owner of the smart contract can mint an NFT using this contract
    function mint(address _to, uint256 _tokenId, string calldata _uri) external onlyOwner {
        require(mintedNFT<=1000, "Max Limit reached"); // This ensures that the max no. of minted NFTs is 1000
        mintedNFT = mintedNFT+1; // To increment the number of NFTs that have been minted uptil now.
        super._mint(_to, _tokenId); // Calls the mint function of the inherited class Ownable
        super._setTokenUri(_tokenId, _uri); //It is used to link the actual NFT data (the JSON file -- specified by URI) to the token ID of the NFT to be minted
    }
 
}
