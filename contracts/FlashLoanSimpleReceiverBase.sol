// SPDX-License-Identifier: AGPL-3.0
pragma solidity 0.8.10;

import {IFlashLoanSimpleReceiver} from "aave/aave-v3-core@1.16.2/contracts/flashloan/interfaces/IFlashLoanSimpleReceiver.sol";
import {IPoolAddressesProvider} from "aave/aave-v3-core@1.16.2/contracts/interfaces/IPoolAddressesProvider.sol";
import {IPool} from "aave/aave-v3-core@1.16.2/contracts/interfaces/IPool.sol";

/**
 * @title FlashLoanSimpleReceiverBase
 * @author Aave
 * @notice Base contract to develop a flashloan-receiver contract.
 */
abstract contract FlashLoanSimpleReceiverBase is IFlashLoanSimpleReceiver {
    IPoolAddressesProvider public immutable override ADDRESSES_PROVIDER;
    IPool public immutable override POOL;

    constructor(IPoolAddressesProvider provider) {
        ADDRESSES_PROVIDER = provider;
        POOL = IPool(provider.getPool());
    }
}
