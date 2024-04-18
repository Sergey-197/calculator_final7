class Division:
    @staticmethod
    def divide_complex_numbers(a, b):
        denominator = b[0] ** 2 + b[1] ** 2
        real = (a[0] * b[0] + a[1] * b[1]) / denominator
        imaginary = (a[1] * b[0] - a[0] * b[1]) / denominator
        return (real, imaginary)