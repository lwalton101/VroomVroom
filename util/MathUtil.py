class MathUtil:
    @staticmethod
    def RoundFloatPosToIntPos(pos: tuple[float, float]) -> tuple[int, int]:
        return (round(pos[0]), round(pos[1]))
