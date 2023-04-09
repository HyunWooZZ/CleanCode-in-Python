from collections import UserDict
import datetime

class TransactionalPolicy(UserDict):
    """Bad case about inheritance.."""
    def change_in_policy(self, customer_id, **new_policy_data):
        self[customer_id].update(**new_policy_data)

if __name__ == "__main__":
    policy = TransactionalPolicy({
        "client": {
            "fee": 1000.0,
            "expiration_date": datetime.datetime(2023, 1, 1, 0, 0)
            }
        }
    )

    print(policy["client"])
    ## There are too many method that doesn`t use in the TrasnationalPolicy...
    print(dir(policy))

    ## There are 2 problem in here..
    ## 1. hierachy structure is Bad
    ## making the new class by base class means that class`s mean is expanded and also more in detail.
    ## but in this case we can`t know this class`s parent is userdict by name..

    ## 2. The Coupling Issue
    ## in above class has the pop() method, items() mtehod and so on..
    ## do we need that all?
    ## absolutely not!!!! and all that method are public so we can use them all..
    ## so the user can call that all method even there are side effect..

    