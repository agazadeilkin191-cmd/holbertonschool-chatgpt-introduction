class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Xəta: Depozit məbləği müsbət olmalıdır.")
            return
        self.balance += amount
        print("Mədaxil edildi: ${:.2f}".format(amount))
        self.get_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Xəta: Çıxarılacaq məbləğ müsbət olmalıdır.")
        elif amount > self.balance:
            print("Xəta: Balansda kifayət qədər vəsait yoxdur.")
        else:
            self.balance -= amount
            print("Məxaric edildi: ${:.2f}".format(amount))
            self.get_balance()

    def get_balance(self):
        print("Cari Balans: ${:.2f}".format(self.balance))

def get_valid_amount(prompt):
    """İstifadəçinin düzgün rəqəm daxil etməsini təmin edir."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Xəta: Zəhmət olmasa düzgün rəqəm daxil edin.")

def main():
    cb = Checkbook()
    print("--- Checkbook Proqramına Xoş Gəlmisiniz ---")
    
    while True:
        action = input("\nNə etmək istəyirsiniz? (deposit, withdraw, balance, exit): ").lower().strip()
        
        if action == 'exit':
            print("Proqram bitdi. Sağ olun!")
            break
        elif action == 'deposit':
            amount = get_valid_amount("Depozit məbləğini daxil edin: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Çıxarmaq istədiyiniz məbləği daxil edin: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Yanlış əmr. Zəhmət olmasa yenidən cəhd edin.")

if __name__ == "__main__":
    main()
