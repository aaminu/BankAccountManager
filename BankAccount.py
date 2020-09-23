"""
Bank Account Manager with normal and ATM type withdrawal
"""

class Account:
    """
    Abstract base class for account types.
    With print function, deposit and withdrawal
    """

    def __init__(self, acct_num: str, open_deposit: float):
        self.acct_num = acct_num
        self.balance = open_deposit

    def __str__(self):
        return f'${self.balance:.2f}'

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('\nFunds not available')


class SavingAccount(Account):
    """
    Savings Account as a child class to Account
    """

    def __init__(self, acct_num: str, open_deposit: float):
        super().__init__(acct_num, open_deposit)

    def __str__(self):
        return f'Saving Account: #{self.acct_num}\n\tBalance: {super().__str__()}'


class CurrentAccount(Account):
    """
    Current Account as a child class to Account
    """

    def __init__(self, acct_num: str, open_deposit: float):
        super().__init__(acct_num, open_deposit)

    def __str__(self):
        return f'Current Account #{self.acct_num}\n\tBalance: {super().__str__()}'


class BusinessAccount(Account):
    """
    Business Account as a child class to Account
    """

    def __init__(self, acct_num: str, open_deposit: float):
        super().__init__(acct_num, open_deposit)

    def __str__(self):
        return f'Business Account #{self.acct_num}\n\tBalance: {super().__str__()}'


class Customer:
    """
    Customer class that hold information about each customer
    """

    def __init__(self, first_name, last_name, middle_name=None):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        if middle_name is not None:
            self.middle_name = middle_name
        self.accounts = {'savings': [], 'current': [], 'business': []}

        # Protected Values, don't call outside Class
        self.__pin = 1234
        self.__accounts = {'savings': [], 'current': [], 'business': []}

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def open_savings_account(self, acct_num, open_deposit=None):
        if open_deposit is None:
            open_deposit = 0
        temp = SavingAccount(acct_num, open_deposit)
        self.__accounts['savings'].append(temp)
        self.accounts['savings'].append(temp.acct_num.lower())

    def open_current_account(self, acct_num, open_deposit):
        try:
            assert open_deposit > 1000
        except AssertionError:
            print('\nMinimum opening balance is #1000, please try again')
        else:
            temp = CurrentAccount(acct_num, open_deposit)
            self.__accounts['current'].append(temp)
            self.accounts['current'].append(temp.acct_num.lower())

    def open_business_account(self, acct_num, open_deposit):
        try:
            assert open_deposit > 5000
        except AssertionError:
            print('\nMinimum opening balance is #5000, please try again')
        else:
            temp = BusinessAccount(acct_num, open_deposit)
            self.__accounts['business'].append(temp)
            self.accounts['business'].append(temp.acct_num.lower())

    def pin_change(self):
        new_pin = 0
        while not self.__pin == new_pin:
            try:
                new_pin = int(input('Enter 4 digit new pin'))
                assert new_pin != self.__pin

            except ValueError:
                print('Please enter only digits')
                new_pin = 0

            except AssertionError as a:
                print('Please use a different 4 digit number')
                new_pin = 0

            else:
                self.__pin = new_pin
                break

    def _acc_verifier(self, acct_num, acct_type):
        """
        verification of account and returns the object of that account.
        This is for internal use alone!!
        """
        acct_num = acct_num.lower()
        acct_type = acct_type.lower()

        try:
            ind = self.accounts[acct_type].index(acct_num)

        except KeyError:
            return '\nPlease Check the account-type and try again'

        except ValueError:
            return '\nPlease Check the account-number and try again'
        else:
            object_name = self.__accounts[acct_type][ind]
            return object_name

    def withdraw(self, acct_num, acct_type, amount):
        user_account = self._acc_verifier(acct_num, acct_type)
        if isinstance(user_account, str):
            print(user_account)
        else:
            user_account.withdrawal(amount)

    def deposit(self, acct_num, acct_type, amount):
        user_account = self._acc_verifier(acct_num, acct_type)
        if isinstance(user_account, str):
            print(user_account)
        else:
            user_account.deposit(amount)

    def get_balance(self, acct_num, acct_type):
        user_account = self._acc_verifier(acct_num, acct_type)
        if isinstance(user_account, str):
            print(user_account)
        else:
            print(user_account)

