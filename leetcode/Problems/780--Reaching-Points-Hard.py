class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        ''' Starting from tx, ty reduce to lesser number
        '''
        
        while(sx < tx and sy < ty):
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        
#         Now reduced to form x, kx+y or x+ky, y
        # print(sx, sy, tx, ty)
        # print((sy == ty and tx >= sx and (tx-sx)%sy == 0))
        # print((sx == tx and ty >= sy and (ty-sy)%sx == 0))
        return (sy == ty and tx >= sx and (tx-sx)%sy == 0) or (sx == tx and ty >= sy and (ty-sy)%sx == 0)