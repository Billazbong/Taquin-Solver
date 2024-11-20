from collections import deque
import heapq

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
    return None

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
    return None

def manhattan_distance(state,k):
    """Calculate the sum of all manhattan distances"""
    distance=0
    for i in range(k):
        for j in range(k):
            value=state[i*k+j]
            if value!=0:
                goal_x,goal_y=divmod(value-1,k)
                distance+= abs(i-goal_x)+abs(j-goal_y)
    return distance

def a_star(taquin):
    """Implement A* algorithm to solve taquin"""
    priority_queue=[]
    heapq.heappush(priority_queue,(0,taquin.tableau,0,None)) #f(n), state, g(n), parent_state
    visited=set([taquin.tableau])
    parent_dict={taquin.tableau:None}
    while priority_queue:
        _,current_state,g,parent_state=heapq.heappop(priority_queue)
        if taquin.final(current_state):
            path=[current_state]
            while parent_state is not None:
                path.append(parent_state)
                parent_state=parent_dict[parent_state]
            path.reverse()
            return path
        for state in taquin.generate_next_states(current_state):
            if state not in visited:
                new_g=g+1
                new_f=new_g+manhattan_distance(state,taquin.k)
                visited.add(state)
                parent_dict[state]=current_state
                heapq.heappush(priority_queue,(new_f,state,new_g,current_state))
    return None