class BankingSystem:
    def __init__(self):
        self.accounts = {}  # Stores account balances
        self.outgoing_transactions = {}  # Tracks total outgoing amounts
        self.payments = {}  # Stores payment details
        self.cashback_schedule = []  # Tracks scheduled cashback
        self.payment_count = 0  # Counts payments for unique IDs
        self.account_history = {}  # Tracks balance history

    def create_account(self, timestamp, account_id):
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = 0
        self.outgoing_transactions[account_id] = 0
        self.account_history[account_id] = [(timestamp, 0)]  # Initialize balance history
        return True

    def deposit(self, timestamp, account_id, amount):
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        self.account_history[account_id].append((timestamp, self.accounts[account_id]))  # Log balance change
        return self.accounts[account_id]

    def transfer(self, timestamp, source_account_id, target_account_id, amount):
        if source_account_id not in self.accounts or target_account_id not in self.accounts:
            return None
        if source_account_id == target_account_id:
            return None
        if self.accounts[source_account_id] < amount:
            return None

        self.accounts[source_account_id] -= amount
        self.accounts[target_account_id] += amount
        self.outgoing_transactions[source_account_id] += amount
        self.account_history[source_account_id].append((timestamp, self.accounts[source_account_id]))
        self.account_history[target_account_id].append((timestamp, self.accounts[target_account_id]))
        return self.accounts[source_account_id]

    def pay(self, timestamp, account_id, amount):
        if account_id not in self.accounts:
            return None
        if self.accounts[account_id] < amount:
            return None

        # Deduct the amount
        self.accounts[account_id] -= amount
        self.outgoing_transactions[account_id] += amount

        # Generate unique payment ID
        self.payment_count += 1
        payment_id = f"payment{self.payment_count}"

        # Schedule cashback
        cashback_amount = amount // 50  # 2% of the amount
        cashback_time = timestamp + 86400000  # 24 hours in milliseconds
        self.cashback_schedule.append((cashback_time, account_id, cashback_amount, payment_id))

        # Store payment details
        self.payments[payment_id] = {
            "account_id": account_id,
            "timestamp": timestamp,
            "cashback_time": cashback_time,
            "cashback_amount": cashback_amount,
            "status": "IN_PROGRESS",
        }

        self.account_history[account_id].append((timestamp, self.accounts[account_id]))
        return payment_id

    def get_payment_status(self, timestamp, account_id, payment):
        if account_id not in self.accounts:
            return None
        if payment not in self.payments:
            return None
        if self.payments[payment]["account_id"] != account_id:
            return None

        # Update cashback status if applicable
        payment_details = self.payments[payment]
        if timestamp >= payment_details["cashback_time"] and payment_details["status"] == "IN_PROGRESS":
            self.accounts[account_id] += payment_details["cashback_amount"]
            payment_details["status"] = "CASHBACK_RECEIVED"
            self.account_history[account_id].append((timestamp, self.accounts[account_id]))

        return payment_details["status"]

    def merge_accounts(self, timestamp, account_id_1, account_id_2):
        if account_id_1 == account_id_2 or account_id_1 not in self.accounts or account_id_2 not in self.accounts:
            return False

        # Transfer balance
        self.accounts[account_id_1] += self.accounts[account_id_2]
        self.account_history[account_id_1].append((timestamp, self.accounts[account_id_1]))

        # Update outgoing transactions
        self.outgoing_transactions[account_id_1] += self.outgoing_transactions[account_id_2]

        # Reassign cashback payments
        for payment_id, payment in self.payments.items():
            if payment["account_id"] == account_id_2:
                payment["account_id"] = account_id_1

        # Update pending cashback schedules
        for cashback in self.cashback_schedule:
            if cashback[1] == account_id_2:
                cashback = (cashback[0], account_id_1, cashback[2], cashback[3])

        # Merge balance history
        self.account_history[account_id_1].extend(self.account_history[account_id_2])
        self.account_history[account_id_1].sort(key=lambda x: x[0])

        # Remove account_id_2
        del self.accounts[account_id_2]
        del self.outgoing_transactions[account_id_2]
        del self.account_history[account_id_2]
        return True

    def get_balance(self, timestamp: int, account_id: str, time_at: int):
        if account_id not in self.account_history:
            return None

        # Find the balance at the given time
        history = self.account_history[account_id]
        for t, balance in reversed(history):
            if t <= time_at:
                return balance
        return None

    def top_spenders(self, timestamp: int, n: int):
        sorted_accounts = sorted(
            self.outgoing_transactions.items(),
            key=lambda x: (-x[1], x[0])
        )
        result = [f"{account_id}<{total_outgoing}>" for account_id, total_outgoing in sorted_accounts]
        return result[:n]

