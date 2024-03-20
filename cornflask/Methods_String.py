class MethodString:

    def __init__(self):
        self.name_input = ""

    def name_inputs(self, word):
        self.name_input = word

    def printString(self):
        return self.name_input.upper()
