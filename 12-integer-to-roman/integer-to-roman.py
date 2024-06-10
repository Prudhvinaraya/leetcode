class Solution:
    def intToRoman(self, num: int) -> str:
        sym = {
            1   : "I",
            4   : "IV",
            5   : "V",
            9   : "IX",
            10  : "X",
            40  : "XL",
            50  : "L",
            90  : "XC",
            100 : "C",
            400 : "CD",
            500 : "D",
            900 : "CM",
            1000 : "M"
        }
        
        values = sym.keys()
        result = []

        for val in reversed(values):
            quo, num = divmod(num, val)
            if quo > 0:
                temp = [sym[val]] * quo
                result.extend(temp)
                        
        return ''.join(result)