from transitions.extensions import GraphMachine
from functools import partial


class Model:

    def clear_state(self, deep=False, force=False):
        print("Clearing state ...")
        return True


model = Model()
machine = GraphMachine(model=model, states=[
    "user", 
    "menu", 
    "movie", 
    "eat", 
    "work_out", 
    "meal", 
    "drink", 
    "dessert", 
    "show_fsm",  
    "random_dessert", 
    "random_drink", 
    "fifteen", 
    "twenty",
    "place1", 
    "place2", 
    ],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {  # movie <->selection
            "trigger": "advance",
            "source": "menu",
            "dest": "movie",
            "conditions": "is_going_to_movie",
        },
        { 
            "trigger": "advance",
            "source": "movie",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        
        { # show_fsm <-> selection
            "trigger": "advance",
            "source": "menu",
            "dest": "show_fsm",
            "conditions": "is_going_to_show_fsm",
        },
        { 
            "trigger": "advance",
            "source": "show_fsm",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        
        
        { # eat <-> selection
            "trigger": "advance",
            "source": "menu",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        { 
            "trigger": "advance",
            "source": "eat",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        
        { # work_out <-> selection
            "trigger": "advance",
            "source": "menu",
            "dest": "work_out",
            "conditions": "is_going_to_work_out",
        },
        { 
            "trigger": "advance",
            "source": "work_out",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        
        { # eat <-> meal
            "trigger": "advance",
            "source": "eat",
            "dest": "meal",
            "conditions": "is_going_to_meal",
        },
        { 
            "trigger": "advance",
            "source": "meal",
            "dest": "place1",
            "conditions": "is_going_to_place1",
        },
        { 
            "trigger": "advance",
            "source": "place1",
            "dest": "meal",
            "conditions": "is_going_to_meal",
        },
        { 
            "trigger": "advance",
            "source": "place1",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        { 
            "trigger": "advance",
            "source": "place1",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        { 
            "trigger": "advance",
            "source": "meal",
            "dest": "place2",
            "conditions": "is_going_to_place2",
        },
        { 
            "trigger": "advance",
            "source": "place2",
            "dest": "meal",
            "conditions": "is_going_to_meal",
        },
        { 
            "trigger": "advance",
            "source": "place2",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        { 
            "trigger": "advance",
            "source": "place2",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        { 
            "trigger": "advance",
            "source": "meal",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        { 
            "trigger": "advance",
            "source": "eat",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        { # eat <-> drink
            "trigger": "advance",
            "source": "eat",
            "dest": "drink",
            "conditions": "is_going_to_drink",
        },
        { 
            "trigger": "advance",
            "source": "drink",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        {   "trigger": "advance",
            "source": "drink",
            "dest": "random_drink",
            "conditions": "is_going_to_random_drink",   
        },
        { 
            "trigger": "advance",
            "source": "random_drink",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        { 
            "trigger": "advance",
            "source": "random_drink",
            "dest": "drink",
            "conditions": "is_going_to_drink",
        },
        { # eat <-> dessert
            "trigger": "advance",
            "source": "eat",
            "dest": "dessert",
            "conditions": "is_going_to_dessert",
        },
        { 
            "trigger": "advance",
            "source": "dessert",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        { 
            "trigger": "advance",
            "source": "random_dessert",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        {   "trigger": "advance",
            "source": "dessert",
            "dest": "random_dessert",
            "conditions": "is_going_to_random_dessert",   
        },
        {   "trigger": "advance",
            "source": "random_dessert",
            "dest": "dessert",
            "conditions": "is_going_to_dessert",   
        },
        { 
            "trigger": "advance",
            "source": "work_out",
            "dest": "fifteen",
            "conditions": "is_going_to_fifteen",
        },
        { 
            "trigger": "advance",
            "source": "fifteen",
            "dest": "work_out",
            "conditions": "is_going_to_work_out",
        },
         { 
            "trigger": "advance",
            "source": "work_out",
            "dest": "twenty",
            "conditions": "is_going_to_twenty",
        },
        { 
            "trigger": "advance",
            "source": "twenty",
            "dest": "work_out",
            "conditions": "is_going_to_work_out",
        }, 
        { ######
            "trigger": "advance", 
            "source": ["menu", "work_out", "movie", "show_fsm", "meal", "drink", "dessert", "random_dessert", "random_drink", "fifteen", "twenty", "place1", "place2"], 
            "dest": "menu",
            "conditions": "is_going_to_menu"
            
        },
    ],
    initial = 'menu',
    auto_transitions= False,
    show_conditions= True,)

model.get_graph().draw('fsm.png', prog='dot')

'''
        { ######
            "trigger": "advance", 
            "source": ["menu", "work_out", "movie", "show_fsm", "meal", "drink", "dessert", "random_dessert", "random_drink", "fifteen", "twenty"], 
            "dest": "user",
            #"conditions": "is_go_back"
            
        },
'''
       
       