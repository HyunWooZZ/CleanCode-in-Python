class TransactionalPolicy:
    """Using the composition example"""
    def __init__(self, policy_data, **extra_data) -> None:
        self._data = {**policy_data, **extra_data}

    def change_in_policy(self, customer_id, **new_policy_data):
        self._data[customer_id].update(**new_policy_data)

    def __getitem__(self, customer_id):
        '''Using the proxy pattern for decrease the coupling'''
        return self._data[customer_id]
    
    def __len__(self):
        return len(self._data)
    