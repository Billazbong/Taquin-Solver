import sys
import random
from collections import deque
import tkinter
import time

class Taquin :
    directions=[(-1,0),(1,0),(0,-1),(0,1)]

    def __init__(self,k):
        self.solution=tuple([(j + 1) % (k * k) for j in range(k*k)])
        self.len=k
        self.tableau=[]
        resolvable=False
        while not resolvable:
            self.generate()
            resolvable=self.solvable()
        self.tableau=tuple(self.tableau)



    def generate(self):
        self.tableau=[0 for _ in range(self.len*self.len)]
        for i in range (self.len*self.len):
            done=0
            while (done==0):
                x=random.randint(0,self.len*self.len-1)
                if (self.tableau[x]==0):
                    self.tableau[x]=i
                    done=1

    def solvable(self):
        swap=0
        copytableau=[x for x in self.tableau if x != 0]
        for i in range(self.len*self.len-1):
            if copytableau[i]!=i+1:
                for j in range(i+1,self.len*self.len-1):
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

        for i in range(self.len):
            for j in range(self.len):
                if (current_state[i*self.len+j]==0):
                    empty_pos=(i,j)
                    break

        for dx,dy in Taquin.directions:
            x,y=empty_pos[0]+dx,empty_pos[1]+dy
            if  0<=x<self.len and 0<=y<self.len:
                new_state=current_state[:]
                new_state[empty_pos[0]*self.len+empty_pos[1]],new_state[x*self.len+y]=new_state[x*self.len+y],new_state[empty_pos[0]*self.len+empty_pos[1]]
                next_states.append(tuple(new_state))

        return next_states

def bfs(taquin):
    queue=deque([(taquin.tableau,None)])
    visited=set([taquin.tableau])
    parent_dict={taquin.tableau:None}
    while queue:
        current_state,parent_state=queue.popleft()
        if taquin.final(current_state):
            path=[current_state]
            while parent_state is not None:
                path.append(parent_state)
                parent_state=parent_dict[parent_state]
            path.reverse()
            return path

        for state in taquin.generate_next_states(current_state):
            if state not in visited:
                visited.add(state)
                parent_dict[state]=current_state
                queue.append((state,current_state))

def dfs(taquin):
    stack=[(taquin.tableau,None)]
    visited=set([taquin.tableau])
    parent_dict={taquin.tableau:None}
    while stack:
        current_state,parent_state=stack.pop()
        if taquin.final(current_state):
            path=[current_state]
            while parent_state is not None:
                path.append(parent_state)
                parent_state=parent_dict[parent_state]
            path.reverse()
            return path


        for state in taquin.generate_next_states(current_state):
            if state not in visited:
                visited.add(state)
                parent_dict[state]=current_state
                stack.append((state,current_state))


def test(algorithme,k):
    for _ in range(1000):
        taquin=Taquin(k)
        if algorithme(taquin) is None :
            return False




print(test(bfs,3))
print("--------------------------------------------------------------")
print(test(dfs,3))
