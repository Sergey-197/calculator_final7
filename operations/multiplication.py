class Multiplication:
    @staticmethod
    def multiply_complex_numbers(a, b):
        return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])