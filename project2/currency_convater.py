
class CurrencyConverter:
    exchange_rates = {
        "USD" : 1.0,
        "BDT" : 121.75,
        "EUR" : 0.88,
        "GBP" : .75
    }

    def __init__(self, amount, from_currency, to_currency):
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()
    
    def convert(self):
        if self.from_currency not in CurrencyConverter.exchange_rates or \
        self.to_currency not in CurrencyConverter.exchange_rates:
            return "Invalid currency not in our system "
        

        base_amount = self.amount / CurrencyConverter.exchange_rates[self.from_currency]
        converted_amount = base_amount * CurrencyConverter.exchange_rates[self.to_currency]
        return round(converted_amount,2)
    
    @classmethod
    def update_rate(cls, currency, new_rate):
        cls.exchange_rates[currency] = new_rate
    
    @staticmethod
    def is_valid_currency(code):
        return code.upper() in CurrencyConverter.exchange_rates
    
class Logger:
    def log(self, user, converter):
        result = converter.convert()
        print(f"record: {user} conterted {converter.amount} {converter.from_currency} -> {result} {converter.to_currency}")


if __name__ == "__main__" :
    amount = float(input("Enter amount: "))
    from_curr = input("Enter Your Currency: ")
    to_curr = input("Enter Your Desired Currency In Which You Want to Convert: ")
    user = input("Enter Your Name: ")

    converter = CurrencyConverter(amount, from_curr, to_curr)

    if not CurrencyConverter.is_valid_currency(from_curr) or not CurrencyConverter.is_valid_currency(to_curr):
        print("Invalid Currency we do nothave that currency")
    else:
        logger = Logger()
        logger.log(user, converter)
        
