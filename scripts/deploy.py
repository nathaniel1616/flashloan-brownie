from scripts.helpful_scripts import get_account
from brownie import network, config, FlashLoan
from web3 import Web3


account = get_account()


def deploy_flashloan():
    account = get_account()
    POOL_ADDRESS_PROVIVER = "0xc4dCB5126a3AfEd129BC3668Ea19285A9f56D15D"
    flashloan = FlashLoan.deploy(POOL_ADDRESS_PROVIVER, {"from": account})
    print("flash loan has been deployed")


def main():
    deploy_flashloan()
