import logic_for_2048 as logic

if __name__ == '__main__':
    print(__name__)
A = logic.new_game()
logic.show_matrix(A)

    
while True:    
    direction = input("Press the command: ")
    
    if direction == "w":
        A, cond = logic.move_up(A)
        
        if logic.get_current_state(A):
            logic.show_matrix(A)
            print(logic.get_current_state(A))
            break
        
        if cond:
            A = logic.add_new_2_or_4(A)
            
        logic.show_matrix(A)
        
        if logic.get_current_state(A):
            print(logic.get_current_state(A))
            break
            
    elif direction == "a":
        A, cond = logic.move_left(A)
        
        if logic.get_current_state(A):
            logic.show_matrix(A)
            print(logic.get_current_state(A))
            break
        
        if cond:
            A = logic.add_new_2_or_4(A)
            
        logic.show_matrix(A)
        
        if logic.get_current_state(A):
            print(logic.get_current_state(A))
            break
        
    elif direction == "s":
        A, cond = logic.move_down(A)
        
        if logic.get_current_state(A):
            logic.show_matrix(A)
            print(logic.get_current_state(A))
            break
        
        if cond:
            A = logic.add_new_2_or_4(A)
            
        logic.show_matrix(A)
        
        if logic.get_current_state(A):
            print(logic.get_current_state(A))
            break
        
    elif direction == "d":
        A, cond = logic.move_right(A)
        
        if logic.get_current_state(A):
            logic.show_matrix(A)
            print(logic.get_current_state(A))
            break
        
        if cond:
            A = logic.add_new_2_or_4(A)
            
        logic.show_matrix(A)
        
        if logic.get_current_state(A):
            print(logic.get_current_state(A))
            break
    
    else:
        print("Wrong input")
        logic.show_matrix(A)
