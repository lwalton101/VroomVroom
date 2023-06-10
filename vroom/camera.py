from typing import Tuple
import pygame


class Camera:
    offset: Tuple[float, float] = 0, 0
    screenWidth: int = -1
    screenHeight: int = -1

    @staticmethod
    def WorldPosToScreenPos(worldPos: tuple[float, float]) -> tuple[int, int]:
        screenPos: tuple[int, int] = (
            round(worldPos[0]) + Camera.screenWidth // 2,
            round(worldPos[1] * -1) + Camera.screenHeight // 2,
        )
        screenPos = (
            screenPos[0] - round(Camera.offset[0]),
            screenPos[1] + round(Camera.offset[1]),
        )
        return screenPos
