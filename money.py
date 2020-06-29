# pylint: disable=unidiomatic-typecheck,unnecessary-pass


class DifferentCurrencyError(Exception):
    pass


class Currency:
  def __init__(self, name, code,  symbol=None, digits=2):
      self.name = name
      self.code = code
      self.symbol = symbol
      self.digits = digits
      
     

  def __str__(self):
    if self.symbol:
      return f"{self.code}({self.symbol})"
      
    else: 
        return f"{self.code}"
        """
        Should return the currency code, or code with symbol in parentheses.
        """
        pass

    def __eq__(self, other):
      """
        All fields must be equal to for the objects to be equal.
        """
      return (type(self) == type(other) and self.name == other.name and
                self.code == other.code and self.symbol == other.symbol and
                self.digits == other.digits)


class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        pass

    def __str__(self):
        
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """
        pass

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """

        return (type(self) == type(other) and self.amount == other.amount and
                self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        pass

    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        pass

    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        pass

    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        pass
