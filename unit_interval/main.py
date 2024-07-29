# the unit interval is the closed interval [0,1], that is, the set of all real numbers
class UnitInterval:
    # 0を下回ると0、1を上回ると1になるように
    def __init__(self, value):
        self.value: float = max(0, min(1, float(value)))

    # UnitInterval + float, UnitInterval + UnitInterval
    def __add__(self, other) -> "UnitInterval":
        result = self.value + float(other)
        return UnitInterval(result)

    # float + UnitInterval
    def __radd__(self, other) -> "UnitInterval":
        return self.__add__(other)

    def __repr__(self) -> str:
        return f"UnitInterval({self.value})"

    # float(UnitInterval)のときに呼び出される
    def __float__(self) -> float:
        return self.value


if __name__ == "__main__":
    # テスト
    a = UnitInterval(0.5)
    b = UnitInterval(0.7)

    print(a + b)  # UnitInterval(1)
    print(a + 3)  # UnitInterval(1)
    print(3 + a)  # UnitInterval(1)
