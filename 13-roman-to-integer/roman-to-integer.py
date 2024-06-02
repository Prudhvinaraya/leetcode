import functools as fn
import operator as op

class Solution:
    lookup_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    ops = {
        False: op.add,
        True: op.sub
    }
    def romanToInt(self, s: str) -> int:
        _, result = fn.reduce(
            lambda state, c:  
                (lambda num, prev_num, result:
                    (num, self.ops[prev_num > num](result, num))
                )(self.lookup_table[c], *state),
            s[::-1],
            (0, 0)  # prev_num, result
        )
        return result