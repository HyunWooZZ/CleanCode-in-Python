from logging import Logger
class MappedRange:
    """특정 숫자 범위에 대해 맵으로 변환하는 클래스"""
    def __init__(self, transformation, start, end):
        self._transforamtion = transformation
        self._wrapped = range(start, end)

    def __getitem__(self, index):
        value = self._wrapped.__getitem__(index)
        result = self._transforamtion(value)
        Logger.info(f"Index {value}: {result}")
        return result
    
    def __len__(self):
        return len(self._wrapped)

if __name__ == "__main__":
    mr = MappedRange(abs, -10, 5)
    mr[0]
    