import pandas as pd

class Questions:
    def __init__(self):
        self.data = pd.read_csv(r'D:/Marta/Documents/pytania_licencjat_matma.csv', sep=';', index_col='Przedmiot')
        self.data.columns = [i+1 for i in range(len(self.data.columns))]

    def get_category(self, name):
        category = self.data.loc[name]
        return list(category[category.notna()])

    def choose_category(self, name):
        self.question = self.get_category(name)
        return self.question
    
