from scripts.helpful_scripts import get_account
from brownie import network, config, interface, FlashLoan, FlashLoanArbitrage, Dex

from web3 import Web3


account = get_account()


def deploy_flashloan():
    account = get_account()
    POOL_ADDRESS_PROVIVER = "0xc4dCB5126a3AfEd129BC3668Ea19285A9f56D15D"
    flashloan = FlashLoan.deploy(POOL_ADDRESS_PROVIVER, {"from": account})
    print(f"flash loan has been deployed at {flashloan.address}")


def deploy_FlashLoanArbitrage():
    account = get_account()
    POOL_ADDRESS_PROVIVER = "0xc4dCB5126a3AfEd129BC3668Ea19285A9f56D15D"
    flashloan = FlashLoanArbitrage.deploy(POOL_ADDRESS_PROVIVER, {"from": account})
    print(f"flash loan  Arbitrage has been deployed at {flashloan.address}")


def deploy_Dex():
    account = get_account()
    dex = Dex.deploy({"from": account})
    print(f"Dex has been deployed at {dex.address}")


def main():
    deploy_FlashLoanArbitrage()
    # deploy_Dex()
