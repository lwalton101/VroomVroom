from typing import Tuple
import pygame

class Camera:
    offset: Tuple[int,int] = 20,0
    screenWidth: int = -1
    screenHeight: int = -1
    
    
    @staticmethod
    def AdjustRectForOffset(rect: pygame.Rect) -> pygame.Rect:
        center: Tuple[int,int] = rect.center
        rect.center = (center[0] + Camera.screenWidth // 2 + Camera.offset[0], center[1] + Camera.screenHeight // 2 + Camera.offset[1])
        return rect
