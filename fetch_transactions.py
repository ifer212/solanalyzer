from solders.pubkey import Pubkey
from solana.rpc.async_api import AsyncClient

# Initialize Solana RPC client
rpc_url = "https://api.mainnet-beta.solana.com"
client = AsyncClient(rpc_url)

async def get_wallet_transactions(wallet_address):
    wallet_pubkey = Pubkey.from_string(wallet_address)
    response = await client.get_signatures_for_address(wallet_pubkey, limit=100)
    return response.value

async def get_transaction_details(signature):
    response = await client.get_transaction(signature)
    return response
