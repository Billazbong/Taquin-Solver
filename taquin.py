import sys
import os
import random
import tkinter
import time
import algorithm
import multiprocessing

class Taquin :
    directions=[(-1,0),(1,0),(0,-1),(0,1)]

    def __init__(self,k):
        self.solution=tuple([(j + 1) % (k * k) for j in range(k*k)])
        self.k=k
        self.tableau=[]
        solvable=False
        while not solvable:
            self.generate()
            solvable=self.solvable()
        self.tableau=tuple(self.tableau)



    def generate(self):
        """Generate a taquin"""
        self.tableau=[0 for _ in range(self.k*self.k)]
        for i in range (self.k*self.k):
            done=0
            while (done==0):
                x=random.randint(0,self.k*self.k-1)
                if (self.tableau[x]==0):
                    self.tableau[x]=i
                    done=1

    def solvable(self):
        """Check if the taquin is solvable or not"""
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
        """Check if the taquin is solved"""
        return state==self.solution


    def generate_next_states(self,state):
        """Generate the next possible states"""
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

def test(algorithm,k,n,result,queue):
    """Start n test of k*k taquin using algorithm"""
    total_time=0
    for _ in range(n):
        taquin=Taquin(k)
        start_time = time.time()
        algorithm(taquin)
        end_time=time.time()
        elapsed_time=end_time-start_time
        total_time+=elapsed_time
        queue.put(1)
    result.append(total_time)
    

def run_multiprocess():
    """Run multiple processes to solve multiple taquin"""
    queue=multiprocessing.Queue()
    manager=multiprocessing.Manager()
    result=manager.list()
    processes=[]
    portion,rest=divmod(n,n_threads)
    for i in range(n_threads):
        portion_to_use=portion+rest if i == 0 else portion
        p=multiprocessing.Process(target=test,args=(chosen_algorithm,k,portion_to_use,result,queue))
        p.start()
        processes.append(p)
        
    total_done=0
    while total_done<n:
        queue.get()
        total_done += 1
        print(total_done)

    for p in processes:
        p.join()
    total_time = sum(result)
    avg_time = total_time / float(n)
    print(f"Average elapsed time to solve: {avg_time:.6f} seconds")


if __name__=="__main__":
    print("How many tries?")
    n=int(input())
    print("Which size?")
    k=int(input())
    chosen_algorithm=None
    while chosen_algorithm is None:
        print("Which algorithm : ")
        print("1. BFS")
        print("2. DFS")
        print("3. A*")
        print("4. BFS (NO LOOP)")
        print("5. DFS (NO LOOP)")
        chosen_algorithm=algorithm.convert_input_to_algo(int(input()))

    if n>1:
        n_threads=int(os.cpu_count()/3)
        run_multiprocess()
    else:
        result=[]
        print(chosen_algorithm(Taquin(k)))

