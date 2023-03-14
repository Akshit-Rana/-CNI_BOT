import random


EMPTY = 0

class player:
    def __init__(self):
        self.step=0
        self.blockLength=4
        self.AstraU = 0
        self.AstraD = 0
        self.AstraR = 0
        self.AstraL = 0

        self.headEast=False
        self.headNorth=False
        self.headWest=False
        self.headSouth=False

        self.wentEast=False
        self.wentWest=False
        self.wentNorth=False
        self.wentSouth=False

    def move(self,B,N,cur_x,cur_y):
        self.step+=1
        #print("Step size = ", self.step)
        if self.step>350:
            self.blockLength=3
        
        

        if self.headEast==False and self.headWest==False and N-cur_x>=4 and B[(cur_x+1)%N][cur_y]==0 and B[(cur_x+2)%N][cur_y]==0 and B[(cur_x+3)%N][cur_y]==0:
            print("Heading East")
            self.headEast=True
        if self.headEast == True and self.AstraL<=self.blockLength and B[(cur_x+1)%N][cur_y]==0:
            return self.goE()    
        if self.headNorth==False and self.headSouth==False and cur_y>=4 and B[cur_x][(cur_y+N-1)%N]==0 and B[cur_x][(cur_y+N-2)%N]==0 and B[cur_x][(cur_y+N-3)%N]==0:
            print("North clear")
            self.headNorth=True
        else:
            print("Permission granted to march south")
            self.headSouth=True

        if self.wentEast==True and self.headNorth==True and self.headEast == True and self.AstraU<=self.blockLength and B[cur_x][(cur_y+N-1)%N]==0:
            return self.goN()
        if self.wentNorth==True and self.headNorth==True and self.headEast == True and self.AstraR<=self.blockLength and B[(cur_x+N-1)%N][cur_y]==0:
            return self.goW()
        if self.wentWest==True and self.headNorth==True and self.headEast == True and self.AstraD<=self.blockLength and B[cur_x][(cur_y+1)%N]==0:
            self.headEast=False
            print("East Conquored via North")
            return self.goS()
        
        # if self.headEast==True and self.headNorth==True:
        #     self.reDir()
        #     self.refresh()
        #     self.headNorth=False

        if self.wentEast==True and self.headEast == True and self.AstraD<=self.blockLength and B[cur_x][(cur_y+1)%N]==0:
            print("Marching south")
            return self.goS()
        if self.wentSouth==True and self.headEast == True and self.AstraR<=self.blockLength and B[(cur_x+N-1)%N][cur_y]==0:
            return self.goW()
        if self.wentWest==True and self.headEast == True and self.AstraU<=self.blockLength and B[cur_x][(cur_y+N-1)%N]==0:
            self.headEast=False
            print("East conquored via south")
            return self.goN()

        self.headEast=False
        self.headNorth=False
        self.headSouth=False
        if self.headWest==False:
            self.refresh()
            self.reDir()

        
        if self.headWest==False and cur_x>=4 and B[(cur_x+N-1)%N][cur_y]==0 and B[(cur_x+N-2)%N][cur_y]==0 and B[(cur_x+N-3)%N][cur_y]==0:
            print("Permission granted to head West")
            self.headWest=True
        
        if self.headWest == True and self.AstraR<=self.blockLength and B[(cur_x+N-1)%N][cur_y]==0:
            print("Marching to west")
            return self.goW()    
        
        if self.headNorth==False and self.headSouth==False and cur_y>=4 and B[cur_x][(cur_y+N-1)%N]==0 and B[cur_x][(cur_y+N-2)%N]==0 and B[cur_x][(cur_y+N-3)%N]==0:
            print("Permission granted to attack west via north")
            self.headNorth=True
        else:
            print("Permission granted to attack west via south")
            self.headSouth=True

        if self.wentWest==True and self.headNorth==True and self.headWest == True and self.AstraU<=self.blockLength and B[cur_x][(cur_y+N-1)%N]==0:
            return self.goN()
        if self.wentNorth==True and self.headNorth==True and self.headWest == True and self.AstraL<=self.blockLength and B[(cur_x+1)%N][cur_y]==0:
            return self.goE()
        if self.wentEast==True and self.headNorth==True and self.headWest == True and self.AstraD<=self.blockLength and B[cur_x][(cur_y+1)%N]==0:
            print("West conquored via north")
            self.headWest=False
            return self.goS()
        
        if self.headWest==True and self.headNorth==True:
            self.reDir()
            self.refresh()
            self.headNorth=False

        # if self.wentWest==True and  self.headWest == True and self.AstraD<=self.blockLength and B[cur_x][(cur_y+1)%N]==0:
        #     return self.goS()
        # if self.wentSouth==True and self.headWest == True and self.AstraL<=self.blockLength and B[(cur_x+1)%N][cur_y]==0:
        #     return self.goE()
        # if self.wentEast==True and self.headWest == True and self.AstraU<=self.blockLength and B[cur_x][(cur_y+N-1)%N]==0:
        #     self.headWest=False
        #     print("West conquored via south")
        #     return self.goN()

        self.headWest=False
        self.headSouth=False
        self.refresh()
        self.reDir()

        # if self.AstraD<=self.blockLength and B[cur_x][(cur_y+1)%N]==0:
        #     return self.goS()
        # if self.AstraR<=self.blockLength and B[(cur_x+N-1)%N][cur_y]==0:
        #     return self.goW()
        # if self.AstraU<=self.blockLength and B[cur_x][(cur_y+N-1)%N]==0:
        #     return self.goN()
        # if self.AstraL<=self.blockLength and B[(cur_x+1)%N][cur_y]==0:
        #     return self.goE()

        # if B[(cur_x+N-1)%N][cur_y]==0:
        #     self.refresh() 
        #     return (-1,0)
            
        # if B[cur_x][(cur_y+N-1)%N]==0:
        #     self.refresh() 
        #     return (0,-1)

        # if B[cur_x][(cur_y+1)%N]==0:
        #     self.refresh() 
        #     return (0,1)

        # if B[(cur_x+1)%N][cur_y]==0:
        #     self.refresh() 
        #     return (1,0)

        # else:

        self.refresh()
        self.reDir() 
        return self.closest_empty(B,N,cur_x,cur_y)

    def goN(self):
        self.AstraU=self.AstraU+1
        if self.AstraU==5:
            self.wentNorth=True
        if self.AstraU==5 and self.AstraD==5 and self.AstraL==5 and self.AstraR==5:
            self.refresh() 
        return (0,-1)
    
    def goS(self):
        self.AstraD=self.AstraD+1
        if self.AstraD==5:
            self.wentSouth=True
        if self.AstraU==5 and self.AstraD==5 and self.AstraL==5 and self.AstraR==5:
            self.refresh() 
        return (0,1)

    def goW(self):
        self.AstraR=self.AstraR+1
        if self.AstraR==5:
            self.wentWest=True
        if self.AstraU==5 and self.AstraD==5 and self.AstraL==5 and self.AstraR==5:
            self.refresh()  
        return (-1,0)
    
    def goE(self):
        self.AstraL=self.AstraL+1
        if self.AstraL==5:
            self.wentEast=True
        if self.AstraU==5 and self.AstraD==5 and self.AstraL==5 and self.AstraR==5:
            self.refresh() 
        return (1,0)

    def refresh(self):
        self.AstraU=0
        self.AstraD=0
        self.AstraR=0
        self.AstraL=0

    def refresh_W(self):
        self.AstraU=0
        self.AstraD=0
        self.AstraL=0

    def refresh_S(self):
        self.AstraU=0
        self.AstraR=0
        self.AstraL=0

    def refresh_N(self):
        self.AstraD=0
        self.AstraR=0
        self.AstraL=0

    def refresh_E(self):
        self.AstraU=0
        self.AstraD=0
        self.AstraR=0

    def reDir(self):
        self.wentWest=0
        self.wentEast=0
        self.wentNorth=0
        self.wentSouth=0

    def closest_empty(self,B,N,cur_x,cur_y):
        dis=2*N+1
        best = {"x":cur_x,"y":cur_y}
        for i in range(N):
            for j in range(N):
                if B[i][j] == EMPTY:
                    dx = min ( abs(cur_x - i) , N - abs(cur_x - i) )
                    dy = min ( abs(cur_y - j) , N - abs(cur_y - j) )
                    cur_dis = dx+dy
                    if cur_dis < dis:
                        dis = cur_dis
                        best["x"] = i 
                        best["y"] = j 

        # Pick the direction to go in

        if best["y"] > cur_y:
            if best["y"]-cur_y < N/2:
                return (0,1)
            else:
                return (0,-1)


        if best["y"] < cur_y:
            if cur_y-best["y"] < N/2:
                return (0,-1)
            else:
                return (0,1)


        if best["x"] > cur_x:
            if best["x"]-cur_x < N/2:
                return (1,0)
            else:
                return (-1,0)

        if best["x"] < cur_x:
            if cur_x-best["x"] < N/2:
                return (-1,0)
            else:
                return (1,0)
        

        return (0,0)
