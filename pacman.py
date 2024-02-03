'''
The Packman Problem
AI lab

'''

import copy 

""" Helper functions for checking operator's conditions """

"Τροποποιώ όλα τα state με σκοπό να λειτουργούν σωστά με το initial state στο κάτω μέρος του προγράμματος"
   
def can_eat(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j][0]=='p' and state[i][j][1]=='f':  
                return 1  

def can_move_right(state):
    return not state[len(state)-1][len(state[0])-1][0]=='p' 

def can_move_left(state):
    return not state[0][0][0]=='p'

def can_move_up(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j][0]=='p':
                return i > 0
    return False

def can_move_down(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j][0]=='p':
                return i < len(state) - 1
    return False


""" Operator function: eat, move right, move left (I added move up, move down) """

def eat(state):
    if can_eat(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j][0]=='p' and state[i][j][1]=='f':  
                    state[i][j][1]=''
                    return state                
    else:
        return state

def move_right(state):
    if can_move_right(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j][0]=='p':
                    state[i][j][0]=''
                    state[i][j+1][0]='p'
                    return state
    else: 
        return state
         
def move_left(state):
    if can_move_left(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j][0]=='p':
                    state[i][j][0]=''
                    state[i][j-1][0]='p'
                    return state
    else:
        return state

def move_up(state):
    if can_move_up(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j][0]=='p':
                    state[i][j][0]=''
                    state[i-1][j][0]='p'
                    return state
    else: 
        return state

def move_down(state):
    if can_move_down(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j][0]=='p':
                    state[i][j][0]=''
                    state[i+1][j][0]='p'
                    return state
    else:
        return state


"Τροποποίω το προγράμμα βάζοντας στο initial state έναν πίνακα 4x4"

initial_state=[[['','f'],['',''],['',''],['','f']], 
               [['',''],['p','f'],['',''],['','']], 
               [['',''],['',''],['',''],['','']]]

print(eat(initial_state),'\n')
print(move_left(initial_state),"\n")
print(move_right(initial_state),"\n")
print(move_up(initial_state),"\n")
print(move_down(initial_state),"\n")


""" ----------------------------------------------------------------------------
******** Search Code for DFS  and other search methods
******** (expanding front only)
******** author:  AI lab
********
******** Κώδικας για DFS και άλλες μεθόδους αναζήτησης
******** (επέκταση μετώπου μόνο)
******** Συγγραφέας: Εργαστήριο ΤΝ
"""

import copy

import sys 
sys.setrecursionlimit(10**6) 

""" ----------------------------------------------------------------------------
**** Problem depending functions
**** ο κόσμος του προβλήματος (αν απαιτείται) και υπόλοιπες συναρτήσεις σχετικές με το πρόβλημα

  #### to be  added ####
"""


""" Helper functions for checking operator's conditions (I added can_move_up, can_move_down)"""

def can_move_right(state):
    for i in range (len(state)):
        res=(state[i][len(state[0])-1][0]=='p') 
        if res==1:
            return 0;
    return 1;

def can_move_left(state):
    for i in range (len(state)):
        res=(state[i][0][0]=='p') 
        if res==1:
            return 0;
    return 1;

def can_move_down(state):
    for i in range (len(state[0])):
        res=(state[len(state)-1][i][0]=='p') 
        if res==1:
            return 0;
    return 1;

def can_move_up(state):
    for i in range (len(state[0])):
        res=(state[0][i][0]=='p') 
        if res==1:
            return 0;
    return 1;

def can_eat(state):
    for y in range(len(state)):
        for x in range(len(state[0])):
            if state[y][x][0]=='p' and state[y][x][1]=='f':  
                return 1 


""" Operator function: eat, move right, move left,(edit: move up, move down) """

def move_right(state):
    if can_move_right(state):
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x][0]=='p':
                    state[y][x][0]=''
                    state[y][x+1][0]='p'
                    return state
    else: 
        return None
    
def move_left(state):
    if can_move_left(state):
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x][0]=='p':
                    state[y][x][0]=''
                    state[y][x-1][0]='p'
                    return state
    else:
        return None

def move_down(state):
    if can_move_down(state):
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x][0]=='p':
                    state[y][x][0]=''
                    state[y+1][x][0]='p'
                    return state
    else:
        return None
    
def move_up(state):
    if can_move_up(state):
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x][0]=='p':
                    state[y][x][0]=''
                    state[y-1][x][0]='p'
                    return state
    else:
        return None

def eat(state):
    if can_eat(state):
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x][0]=='p' and state[y][x][1]=='f':  
                    state[y][x][1]=''
                    return state                
    else:
        return None

""" Function that checks if current state is a goal state """

def is_goal_state(state):
    for x in range(len(state[0])):
        for y in range (len(state)):
            if state[y][x][1]=='f':
                return 0
    return 1

""" Function that finds the children of current state """

'I added the move_up and move_down children'

def find_children(state):

    children=[]  

    up_state=copy.deepcopy(state)
    child_up=move_up(up_state)
    down_state=copy.deepcopy(state)
    child_down=move_down(down_state)
    left_state=copy.deepcopy(state)
    child_left=move_left(left_state)
    right_state=copy.deepcopy(state)
    child_right=move_right(right_state)
    eat_state=copy.deepcopy(state)
    child_eat=eat(eat_state)

    if not child_up==None:
        children.append(child_up)
               
    if not child_down==None:
        children.append(child_down)
        
    if not child_left==None:
        children.append(child_left)
        
    if not child_right==None:
        children.append(child_right)
               
    if not child_eat==None:
        children.append(child_eat)
    
    return children

""" ----------------------------------------------------------------------------
**** FRONT
**** Διαχείριση Μετώπου
"""

""" ----------------------------------------------------------------------------
** initialization of front
** Αρχικοποίηση Μετώπου
"""

def make_front(state):
    return [state]
    
""" ----------------------------------------------------------------------------
**** expanding front
**** επέκταση μετώπου    
"""

def expand_front(front, method):  
    if method=='DFS':        
        if front:
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node):     
                front.insert(0,child)

    #elif method=='BestFS':
    #else: "other methods to be added"        
    
    return front
    

""" ----------------------------------------------------------------------------
**** QUEUE
**** Διαχείριση ουράς
"""

""" ----------------------------------------------------------------------------
** initialization of queue
** Αρχικοποίηση ουράς
"""

def make_queue(state):
    return [[state]]

""" ----------------------------------------------------------------------------
**** expanding queue
**** επέκταση ουράς
"""

def extend_queue(queue, method):
    if method=='DFS':
        print("Queue:")
        print(queue)
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1])
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0,path)

   #queue_copy.........
   #elif method=='BestFS':
   #else: "other methods to be added" 
    
    return queue_copy

""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
**** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
"""

def find_solution(front, queue, closed, goal, method):
       
    if not front:
        print('_NO_SOLUTION_FOUND_')
    
    elif front[0] in closed:
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, goal, method)
    
    #elif is_goal_state(front[0]):
    elif front[0]==goal:
        print('_GOAL_FOUND_')
        print(queue[0])
    
    else:
        closed.append(front[0])
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        queue_copy=copy.deepcopy(queue)
        queue_children=extend_queue(queue_copy, method)
        closed_copy=copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, goal, method)
        
        
"""" ----------------------------------------------------------------------------
** Executing the code
** κλήση εκτέλεσης κώδικα
"""     
def main():


    initial_state=[[['p',''],['','f'],['',''],['','f']],
                    [['','f'],['',''],['f',''],['','']]] 
                    
    goal=         [[['',''],['',''],['',''],['','']],
                   [['',''],['',''],['',''],['p','']]]

    
    method='DFS'
    
    """ ----------------------------------------------------------------------------
    **** starting search
    **** έναρξη αναζήτησης
    """
    
    print('____BEGIN__SEARCHING____')
    find_solution(make_front(initial_state), make_queue(initial_state), [], goal, method)

if __name__ == "__main__":
    main()
    
    initial_state=[[['p',''],['','f'],['',''],['','f']],
                    [['','f'],['',''],['f',''],['','']]] 
                    
    goal=         [[['',''],['',''],['',''],['','']],
                   [['',''],['',''],['',''],['','p']]]



""" ----------------------------------------------------------------------------
******** Search Code for DFS  and other search methods
******** (expanding front only)
******** author:  AI lab
********
******** Κώδικας για DFS και άλλες μεθόδους αναζήτησης
******** (επέκταση μετώπου μόνο)
******** Συγγραφέας: Εργαστήριο ΤΝ
"""

import copy

import sys 
sys.setrecursionlimit(10**6) 

""" ----------------------------------------------------------------------------
**** Problem depending functions
**** ο κόσμος του προβλήματος (αν απαιτείται) και υπόλοιπες συναρτήσεις σχετικές με το πρόβλημα

  #### to be  added ####
"""


""" Helper functions for checking operator's conditions (I added can_move_up, can_move_down) """

def can_move_right(state):
    for i in range (len(state)):
        res=(state[i][len(state[0])-1][0]=='p') 
        if res==1:
            return 0;
    return 1;

def can_move_left(state):
    for i in range (len(state)):
        res=(state[i][0][0]=='p') 
        if res==1:
            return 0;
    return 1;

def can_move_down(state):
    for i in range (len(state[0])):
        res=(state[len(state)-1][i][0]=='p') 
        if res==1:
            return 0;
    return 1;

def can_move_up(state):
    for i in range (len(state[0])):
        res=(state[0][i][0]=='p') 
        if res==1:
            return 0;
    return 1;

def can_eat(state):
    for y in range(len(state)):
        for x in range(len(state[0])):
            if state[y][x][0]=='p' and state[y][x][1]=='f':  
                return 1 


""" Operator function: eat, move right, move left ,(I added move up , move down) """

def move_right(state):
    if can_move_right(state):
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x][0]=='p':
                    state[y][x][0]=''
                    state[y][x+1][0]='p'
                    return state
    else: 
        return None
    
def move_left(state):
    if can_move_left(state):
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x][0]=='p':
                    state[y][x][0]=''
                    state[y][x-1][0]='p'
                    return state
    else:
        return None

def move_down(state):
    if can_move_down(state):
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x][0]=='p':
                    state[y][x][0]=''
                    state[y+1][x][0]='p'
                    return state
    else:
        return None
    
def move_up(state):
    if can_move_up(state):
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x][0]=='p':
                    state[y][x][0]=''
                    state[y-1][x][0]='p'
                    return state
    else:
        return None

def eat(state):
    if can_eat(state):
        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x][0]=='p' and state[y][x][1]=='f':  
                    state[y][x][1]=''
                    return state                
    else:
        return None



""" Function that checks if current state is a goal state (edit: move up, move down) """

def is_goal_state(state):
    for x in range(len(state[0])):
        for y in range (len(state)):
            if state[y][x][1]=='f':
                return 0
    return 1

""" Function that finds the children of current state, I added the move_up and move_down children """

def find_children(state):
    children=[]
    right_state=copy.deepcopy(state)
    child_right=move_right(right_state)
    left_state=copy.deepcopy(state)
    child_left=move_left(left_state)
    eat_state=copy.deepcopy(state)
    child_eat=eat(eat_state)
    up_state=copy.deepcopy(state)
    child_up=move_up(up_state)
    down_state=copy.deepcopy(state)
    child_down=move_down(down_state)


    if not child_right==None:
        children.append(child_right)

    if not child_left==None:
        children.append(child_left)  
        
    if not child_eat==None:
        children.append(child_eat)

    if not child_up==None:
        children.append(child_up)

    if not child_down==None:
        children.append(child_down)  
        

    return children

""" ----------------------------------------------------------------------------
**** FRONT
**** Διαχείριση Μετώπου
"""

""" ----------------------------------------------------------------------------
** initialization of front
** Αρχικοποίηση Μετώπου
"""

def make_front(state):
    return [state]
    
""" ----------------------------------------------------------------------------
**** expanding front
**** επέκταση μετώπου    
"""

def expand_front(front, method):  
    if method=='DFS':        
        if front:
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node):     
                front.insert(0,child)

    elif method=='BFS':        
        if front:
            print("Front:")
            print(front)
            node=front.pop(0) 
            for child in find_children(node): 
                front.append(child) 
    #elif method=='BestFS':
    #else: "other methods to be added"        
    
    return front
    #elif method=='BestFS':
    #else: "other methods to be added"        
    
    return front

""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
**** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
"""

def find_solution(front, closed, goal, method):
       
    if not front:
        print('_NO_SOLUTION_FOUND_')
    
    elif front[0] in closed:
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        find_solution(new_front, closed, goal, method)
    
    #elif is_goal_state(front[0]):
    elif front[0]==goal:
        print('_GOAL_FOUND_')
        print(front[0])
    
    else:
        closed.append(front[0])
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        closed_copy=copy.deepcopy(closed)
        find_solution(front_children, closed_copy, goal, method)
        

 
"""" ----------------------------------------------------------------------------
** Executing the code
** κλήση εκτέλεσης κώδικα
"""
           
def main():


    initial_state=[[['p',''],['',''],['','f'],['','']],
                    [['',''],['','f'],['',''],['','']]] 
    goal=         [[['',''],['',''],['',''],['','']],
                   [['',''],['',''],['',''],['p','']]] 

    
    method='DFS'
    
    """ ----------------------------------------------------------------------------
    **** starting search
    **** έναρξη αναζήτησης
    """
    
    print('____BEGIN__SEARCHING____')
    find_solution(make_front(initial_state), [], goal, method)


if __name__ == "__main__":
    main()
    
    initial_state=[[['p',''],['','f'],['',''],['','f']],
                    [['','f'],['',''],['','f'],['','']]] 
    goal=         [[['',''],['',''],['',''],['','']],
                   [['',''],['',''],['',''],['p','']]]

