import sys
import random
import tkinter
import time
import algorithm


class Taquin :
    directions=[(-1,0),(1,0),(0,-1),(0,1)]

    def __init__(self,k):
        self.solution=tuple([(j + 1) % (k * k) for j in range(k*k)])
        self.k=k
        self.tableau=[]
        resolvable=False
        while not resolvable:
            self.generate()
            resolvable=self.solvable()
        self.tableau=tuple(self.tableau)



    def generate(self):
        self.tableau=[0 for _ in range(self.k*self.k)]
        for i in range (self.k*self.k):
            done=0
            while (done==0):
                x=random.randint(0,self.k*self.k-1)
                if (self.tableau[x]==0):
                    self.tableau[x]=i
                    done=1

    def solvable(self):
        swap=0
        copytableau=[x for x in self.tableau if x != 0]
        for i in range(self.k*self.k-1):
            if copytableau[i]!=i+1:
                for j in range(i+1,self.k*self.k-1):
                    if copytableau[j]==i+1:
                        copytableau[j],copytableau[i]=copytableau[i],copytableau[j]
                        swap+=1
                        break
        return True if swap%2==0 else False

    def final(self,state):
        return state==self.solution


    def generate_next_states(self,state):
        current_state=list(state)
        next_states=[]
        empty_pos=(0,0)

        for i in range(self.k):
            for j in range(self.k):
                if (current_state[i*self.k+j]==0):
                    empty_pos=(i,j)
                    break

        for dx,dy in Taquin.directions:
            x,y=empty_pos[0]+dx,empty_pos[1]+dy
            if  0<=x<self.k and 0<=y<self.k:
                new_state=current_state[:]
                new_state[empty_pos[0]*self.k+empty_pos[1]],new_state[x*self.k+y]=new_state[x*self.k+y],new_state[empty_pos[0]*self.k+empty_pos[1]]
                next_states.append(tuple(new_state))

        return next_states


def test(algorithme,k):
    taquin=Taquin(k)
    start_time = time.time()
    solution=algorithme(taquin)
    end_time=time.time()
    elapsed_time=end_time-start_time

    if solution:
        print("Path found in",len(solution)-1,"steps:")
        for step in solution:
            print(step)

    print(f"Time taken to solve : {elapsed_time:.4f} seconds")
    return elapsed_time

avg_time=0

for _ in range(100):
    avg_time+=test(algorithm.a_star,4)
avg_time=avg_time/100
print(f"Average elapsed time to solve : {avg_time:.4f} seconds")