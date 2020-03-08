class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hAngle = hour * 30.0
        mAngle = minutes*6.0
        hAngle += (minutes*0.5)
        
        return float(min(abs(hAngle - mAngle), 360-abs(hAngle-mAngle)))