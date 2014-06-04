__author__ = 'Aravind Singirikonda'


class Transaction():

    amount = 0.00
    tags = list()
    tranctype = ""

    def __init__(self, amount, tags, tranctype):
        self.amount = amount
        self.tags = tags
        self.tranctype = tranctype
        self.save_to_file()

    def save_to_file(self):
        f = open("files/transactions.csv", "a")
        f.write(str(self.amount)+","+'|'.join(self.tags)+","+self.tranctype+"\n")
        f.close()





