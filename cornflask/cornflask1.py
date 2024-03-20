from math import sqrt


class Calculate:
    def __init__(self):
        self.Q = 3

    def calculate_formula(self, *sample_input):
        C = 50
        H = 30
        for D in sample_input:
            Q = sqrt((2 * C * D / H))
            print(f'{int(Q)}', end=" , ")


calculate = Calculate()
calculate.calculate_formula(100,150,180)

