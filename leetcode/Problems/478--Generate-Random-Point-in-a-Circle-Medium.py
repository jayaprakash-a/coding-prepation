import numpy as np
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.c = [x_center, y_center]

    def randPoint(self) -> List[float]:
        r = self.r*(math.sqrt(random.uniform(0,1)))
        theta = random.uniform(0,360)
        return [r*np.cos(np.deg2rad(theta)) + self.c[0], r*np.sin(np.deg2rad(theta))+self.c[1]]
# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()