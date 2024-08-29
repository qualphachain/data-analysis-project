import requests
from web3 import Web3
import traceback
from dotenv import load_dotenv
import os

load_dotenv()


class BlockDataFetcher: 
    """
    Client for fetching block data using Web3 and Etherscan API.
    """

    def __init__(self, eth_rpc_url=None, etherscan_api_key=None):
        self.web3 = Web3(Web3.HTTPProvider(eth_rpc_url)) if eth_rpc_url else None
        self.etherscan_api_key = etherscan_api_key
        self.base_url = "https://api.etherscan.io/api"

    def get_block_with_web3(self, block_identifier="latest"):
        """
        Fetches block data using Web3.

        Args:
            block_identifier (str or int, optional): The block identifier (number or 'latest'). Default is 'latest'.

        Returns:
            dict: The block data.
        """
        if not self.web3:
            raise ValueError("Web3 provider not configured.")

        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node.")

        block = self.web3.eth.get_block(block_identifier, full_transactions=True)
        return block

    def get_block_with_etherscan(self, block_number):
        """
        Fetches block data using Etherscan API.

        Args:
            block_number (int): The block number to fetch.

        Returns:
            dict: The block data.
        """
        if not self.etherscan_api_key:
            raise ValueError("Etherscan API key not configured.")

        try:
            params = {
                "module": "proxy",
                "action": "eth_getBlockByNumber",
                "tag": hex(block_number),
                "boolean": "true",
                "apikey": self.etherscan_api_key,
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            block = response.json()

            if "error" in block or "result" not in block:
                raise ValueError("Failed to fetch block data from Etherscan API.")

            return block["result"]

        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
            print(traceback.format_exc())
            return None

    def print_block_info(self, block, from_web3=True):
        """
        Prints block information.

        Args:
            block (dict): The block data.
            from_web3 (bool, optional): True if data is from Web3, False if from Etherscan API.
        """
        try:
            if from_web3:
                print(f"Block Number: {block['number']}")
                print(f"Timestamp: {block['timestamp']}")
                print(f"Transactions: {len(block['transactions'])}")
            else:
                print(f"Block Number: {int(block['number'], 16)}")
                print(f"Timestamp: {int(block['timestamp'], 16)}")
                print(f"Transactions: {len(block['transactions'])}")
        except KeyError as e:
            print(f"Error printing block info: {e}")
            print(traceback.format_exc())

    def fetch_and_print_block(self, block_identifier="latest", from_web3=True):
        """
        Fetches block data and prints it.

        Args:
            block_identifier (str or int, optional): The block identifier (number or 'latest'). Default is 'latest'.
            from_web3 (bool, optional): True to use Web3, False to use Etherscan API.
        """
        try:
            if from_web3:
                block = self.get_block_with_web3(block_identifier)
            else:
                block = self.get_block_with_etherscan(block_identifier)

            self.print_block_info(block, from_web3=from_web3)

        except Exception as e:
            print(f"Error fetching and printing block: {e}")
            print(traceback.format_exc())


# Example usage
if __name__ == "__main__":
    eth_rpc_url = "https://mainnet.infura.io/v3/c105943b3ce548ceb7dcfb715f25cef5"
    etherscan_api_key = "2AF58TXHQKCWAVHXYP7MGGBVI4KSUGX5AJ"

    fetcher = BlockDataFetcher(
        eth_rpc_url=eth_rpc_url, etherscan_api_key=etherscan_api_key
    )

    # Fetch and print block using Web3
    fetcher.fetch_and_print_block(block_identifier=20559891, from_web3=True)

    # Fetch and print block using Etherscan
    block_number = 20559891  # Replace with your block number
    fetcher.fetch_and_print_block(block_identifier=block_number, from_web3=False)