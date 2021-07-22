class MissingRanges:

    def __init__(self,lower,upper):
        self.lower = lower
        self.upper = upper

    def add_ranges(self,lower,upper):
        if lower == upper:
            return f'{lower}'
        else:
            return f'{lower}->{upper}'

    def get_missing_ranges(self,array):
        if not array:
            return 

        array_length = len(array)
        res = []
        prev = self.lower - 1
        for i in range(array_length+1):
            if i == array_length:
                curr = self.upper + 1
            else:
                curr = array[i]
            if curr - prev >= 2:
                res.append(self.add_ranges(prev + 1, curr - 1))

            prev = curr

        return res

OBJ = MissingRanges(0,99)
ARRAY = [0, 1, 3, 50, 75]

result = OBJ.get_missing_ranges(ARRAY)
print(result)
        