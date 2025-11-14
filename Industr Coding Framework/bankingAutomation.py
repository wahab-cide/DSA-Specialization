"""
# Bank Automation Problem

## Description

You've been asked to program a bot for a popular bank that will automate the management of incoming requests. 
Every request has its own `timestamp` in seconds, and it is guaranteed that all requests come sequentially, i.e. the timestamp is strictly increasing. 
There are two types of incoming requests:

- **deposit <timestamp> <holder_id> <amount>** — request to deposit `<amount>` amount of money in the `<holder_id>` account;

- **withdraw <timestamp> <holder_id> <amount>** — request to withdraw `<amount>` amount of money from the `<holder_id>` account. 
As a bonus, bank also provides a cashback policy — 2% of the withdrawn amount rounded down to the nearest integer will be returned to the account 
exactly 24 hours after the request timestamp. If the cashback and deposit/withdrawal happen at the same timestamp, assume cashback happens earlier.

Your system should also handle invalid requests. There are two types of invalid requests:

- invalid account number;
- withdrawal of a larger amount of money than is currently available.

For the given list of initial `balances` and `requests`, return the state of `balances` straight after the last request has been processed, 
or an array of a single element `[-<request_id>]` (please note the minus sign), where `<request_id>` is the 1-based index of the first invalid request. 
Note that cashback requests which haven't happened before the last request should be ignored.

---

## Example 1

For `balances = [1000, 1500]` and 
`requests = ["withdraw 1613327630 2 480", "withdraw 1613327644 2 800", "withdraw 1614105244 1 100", "deposit 1614108844 2 200", "withdraw 1614108845 2 150"]`, 
the output should be `solution(balances, requests) = [900, 295]`.

### Explanation

Here are the states of `balances` after each request:

- initially: `[1000, 1500]`;
- `"withdraw 1613327630 2 480"`: `[1000, 1020]`;
- `"withdraw 1613327644 2 800"`: `[1000, 220]`;
- At `1613414030` the 2nd account will receive the cashback of `480 * 0.02 = 9.6`, which is rounded down to `9`: `[1000, 229]`;
- At `1613414044` the 2nd account will receive the cashback of `800 * 0.02 = 16`: `[1000, 245]`;
- `"withdraw 1614105244 1 100"`: `[900, 245]`;
- `"deposit 1614108844 2 200"`: `[900, 445]`;
- `"withdraw 1614108845 2 150"`: `[900, 295]`, which is the answer.
- Cashbacks for the last two withdrawals happen at `1614191644` and `1614195245`, which is after the last request timestamp `1614108845`, so they are ignored.

---

## Example 2

For `balances = [20, 1000, 500, 40, 90]` and `requests = ["deposit 1613327630 3 400", "withdraw 1613327635 1 20", "withdraw 1613327651 1 50", "deposit 1613327655 1 50"]`, the output should be `solution(balances, requests) = [-3]`.

### Explanation

Here are the states of `balances` after each request:

- initially: `[20, 1000, 500, 40, 90]`;
- `"deposit 1613327630 3 400"`: `[20, 1000, 900, 40, 90]`;
- `"withdraw 1613327635 1 20"`: `[0, 1000, 900, 40, 90]`;
- `"withdraw 1613327651 1 50"`: it is not possible to withdraw `50` from the 1st account, so the request is invalid.
- the rest of the requests are not processed

---

## Input/Output

- **[execution time limit]** 4 seconds (js)
- **[memory limit]** 1 GB
- **[input] array.integer balances**

"""



import math
from typing import List

def solution(balances: List[int], requests: List[str]) -> List[int]:
    # Create a copy of balances to work with
    current_balances = balances.copy()
    n = len(current_balances)
    
    # Dictionary to store pending cashbacks: timestamp -> list of (account_id, amount)
    cashbacks = {}
    
    # Process each request
    for request_id, request in enumerate(requests, 1):
        parts = request.split()
        operation = parts[0]
        timestamp = int(parts[1])
        account_id = int(parts[2]) - 1  # Convert to 0-based index
        amount = int(parts[3])
        
        # Check if account_id is valid
        if account_id < 0 or account_id >= n:
            return [-request_id]
        
        if operation == "deposit":
            current_balances[account_id] += amount
            
        elif operation == "withdraw":
            # Check if sufficient funds
            if current_balances[account_id] < amount:
                return [-request_id]
            
            current_balances[account_id] -= amount
            
            # Schedule cashback for 24 hours later (24 * 60 * 60 = 86400 seconds)
            cashback_timestamp = timestamp + 86400
            cashback_amount = math.floor(amount * 0.02)
            
            if cashback_amount > 0:
                if cashback_timestamp not in cashbacks:
                    cashbacks[cashback_timestamp] = []
                cashbacks[cashback_timestamp].append((account_id, cashback_amount))
    
    # Get the last request timestamp to know which cashbacks to apply
    last_timestamp = int(requests[-1].split()[1])
    
    # Apply cashbacks that occur before or at the last timestamp
    # Sort cashback timestamps to process in order
    for cashback_ts in sorted(cashbacks.keys()):
        if cashback_ts <= last_timestamp:
            for account_id, cashback_amount in cashbacks[cashback_ts]:
                current_balances[account_id] += cashback_amount
    
    return current_balances

# Test with the provided examples
if __name__ == "__main__":
    # Example 1
    balances1 = [1000, 1500]
    requests1 = [
        "withdraw 1613327630 2 480",
        "withdraw 1613327644 2 800", 
        "withdraw 1614105244 1 100",
        "deposit 1614108844 2 200",
        "withdraw 1614108845 2 150"
    ]
    result1 = solution(balances1, requests1)
    print(f"Example 1: {result1}")  # Expected: [900, 295]
    
    # Example 2
    balances2 = [20, 1000, 500, 40, 90]
    requests2 = [
        "deposit 1613327630 3 400",
        "withdraw 1613327635 1 20",
        "withdraw 1613327651 1 50",
        "deposit 1613327655 1 50"
    ]
    result2 = solution(balances2, requests2)
    print(f"Example 2: {result2}")  # Expected: [-3]