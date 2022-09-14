import numpy as np
import pickle

class dum():
    def __init__(self, data):
        self.data = data

    def model_load(self):
        with open(r'artifacts/model.pkl', 'rb') as file:
            self.model = pickle.load(file)

    def predict(self):
        self.model_load()
        alcohol = float(self.data['alcohol'])
        malic_acid = float(self.data['malic_acid'])
        ash = float(self.data['ash'])
        alcalinity_of_ash = float(self.data['alcalinity_of_ash'])
        magnesium = float(self.data['magnesium'])
        total_phenols = float(self.data['total_phenols'])
        flavanoids = float(self.data['flavanoids'])
        nonflavanoid_phenols = float(self.data['nonflavanoid_phenols'])
        proanthocyanins = float(self.data['proanthocyanins'])
        color_intensity = float(self.data['color_intensity'])
        hue = float(self.data['hue'])
        diluted_wines = float(self.data['diluted_wines'])
        proline = float(self.data['proline'])
    
        array = np.array([[alcohol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols, flavanoids, nonflavanoid_phenols, proanthocyanins, color_intensity, hue, diluted_wines, proline]])
        result = self.model.predict(array)

        if result[0] == 0:
            print("Red Wine")
            return "Red wine"

        if result[0] == 1:
            print('White wine')
            return "White wine"

        if result[0] == 2:
            print("Black wine")
            return "Black wine"
        
        return result