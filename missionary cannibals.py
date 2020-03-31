#Missionary and cannibals using python in ai
import math
class State():
    def __init__(self,cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight):
        self.cannibalLeft=cannibalLeft
        self.missionaryLeft=missionaryLeft
        self.boat=boat
        self.cannibalRight=cannibalRight
        self.missionaryRight=missionaryRight
        self.parent= None

    def is_goal(self):
        if self.cannibalLeft == 0 and self.missionaryLeft == 0:
            return True
        else:
            return False
    def is_valid(self):
        if self.missionaryLeft >=0 and self.missionaryRight >=0 and self.cannibalLeft >=0 and self.cannibalRight >=0 and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) and (self.missionaryRight ==0 or self.missionaryRight >= self.cannibalRight):
           return True
        else:
            return False
    def __eq__(self,other):
        return self.cannibalLeft==other.cannibalLeft and self.missionaryLeft==other.missionaryLeft and self.boat==other.boat and self.cannibalRight==other.cannibalRight and self.missionaryRight==other.missionaryRight
    def __hash__(self):
        return hash((self.cannibalLeft,self.missionaryLeft,self.boat,self.cannibalRight,self.missionaryRight))
def successors(current_state):
    children==[];
    if current_state.boat=='left':
        new_state=State(current_state.cannibalLeft,current_state.missionaryLeft-2,'right',current_state.cannibalRight,current_state.missionaryRight+2)
    
        if new_state.is_valid():
             new_state.parent=current_state
             children.append(new_state)
        new_state=State(current_state.cannibalLeft -2,current_state.missionaryLeft,'right',current_stata.cannibalRight+2,current_state.missionaryRight)
    
        if new_state.is_valid():
             new_state.parent=current_state
             children.append(new_state)
        new_state=State(current_state.cannibalLeft-1,current_state.missionaryLeft-1,'right',current_state.cannibalRight+1,current_state.missionaryRight+1)
    
        if new_state.is_valid():
             new_state.parent=current_state
             children.append(new_state)
        new_state=State(current_state.cannibal_Left,current_state.missionaryLeft-1,'right',current_state.cannibalRight,current_state.missionarRight+1)
    
        if new_state.is_vaid():
             new_state.parent=current_state
             children.append(new_state)
        new_state=State(current_state.cannibalLeft-1,current_state.missionaryLeft,'right',current_state.cannibalRight+1,current_state.missionaryRight)

        if new_state.is_valid():
             new_state.parent=current_state
             children.append(new_state)
    else:
        new_state=State(current_state.cannibalLeft,current_state.missionaryLeft+2,'left',current_state.cannibalRight,current_state.missionaryRight-2)
    
        if new_state.is_valid():
               new_state.parent=cur_state
               children.append(new_state)
        new_state=State(current_state.cannibalLeft+2,current_state.missionaryLeft,'left',current_state.cannibalRight-1,current_state.missionaryRight-1)
              
        if new_state.is_valid():
               new_state.parent=current_state
               children.append(new_state)
        new_state=State(current_state.cannibalLeft+1,current_state.missionaryLeft+1,'left',current_state.cannibalRight-1,current_state.missionaryRight-1)
              
        if new_state.is_valid():
               new_state.parent=cur_state
               children.append(new_state)
        new_state=State(current_state.cannibalLeft,current_state.missionaryLeft+1,'left',current_state.cannibalRight,current_state.missionaryRight-1)
              
        if new_state.is_valid():
               new_state.parent=current_state
               children.append(new_state)
        new_state=State(current_state.cannibalLeft+1,current_state.missionaryLeft,'left',current_state.cannibalRight-1,current_state.missionaryRight)
              
        if new_state.is_valid():
               new_state.parent=current_state
               children.append(new_state)
               return children
def breadth_first_search():
    initial_state=State(3,3,'left',0,0)
    if initial_state.is_goal():
       return initial_state
       frontier = list()
       explored = set()
       frontier.append(initial_state)
    while frontier:
        state=frontier.pop(0)
        if state.is_goal():
            return state
            explored.add(state)
            children=successors(state)
            for child in children:
                if(child not in explored)or(child not in frontier):
                    frontier.append(child)
    return None
def print_solution(solution):
    path=[]
    path.append(solution)
    parent=solution.parent
    while parent:
        path.append(parent)
        parent=parent.parent
        
        for t in range(len(path)):
            state=path[len(path)-t-1]
            print("("+ str(state.cannibalLeft)+","+ str(state.missionaryLeft)+","+state.boat+","+str(state.cannibalRight)+","+str(state.missionaryRight)+")")
def main():
    solution = breadth_first_search()
    print("Missionaries and Cannibals solution.")
    print("(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)")
    print_solution(solution)

if __name__=="__main__":
    main()
        
            
                 
