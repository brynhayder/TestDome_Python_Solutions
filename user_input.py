NUMERIC_CHARS = "0123456789"

def contains(set1, set2):
    return set1.intersection(set2) == set2

class TextInput:
    def __init__(self):
        self.value = ""

    def add(self, char):
        self.value += char
    
    def get_value(self):
        return self.value
  
class NumericInput(TextInput):
    def add(self, char):
        if contains(NUMERIC_CHARS, set(char)):
            super().add(char)

if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())
