################
# HANOI TOWERS #
################

def hanoi_towers(num_of_disks,peg_start,peg_dest,peg_aux):
    
    """
    Recursive function to solve the Towers of Hanoi problem.
    
    Parameters:
    num_of_disks (integer): Number of disks to move
    peg_start (string): The peg where disks start
    peg_dest (string): The target peg where disks need to go
    peg_aux (string): The auxiliary peg used for temporary holding
    """
    # Base case: if only one disk remains, move it directly to the destination
    if num_of_disks == 1:
        print("Disk 1 moves from ",peg_start," to ",peg_dest)
    else:
        # Step 1: Move (n-1) disks from start peg to auxiliary peg
        hanoi_towers(num_of_disks-1,peg_start,peg_aux,peg_dest)
        
        # Step 2: Move the nth (largest) disk from start peg to destination peg
        print("Disk ",num_of_disks," moves from ",peg_start," to ",peg_dest)
        
        # Step 3: Move the (n-1) disks from auxiliary peg to destination peg
        hanoi_towers(num_of_disks-1,peg_aux,peg_dest,peg_start)
        
while True:
    # Prompt the user to enter the desired number of disks
    num_of_disks = input("Enter the number of disks\n")
    
     # Check whether the user's input is valid (in this case, a positive integer). If the user has entered a letter, a punctation mark, a symbol, a non-integer number, zero, or a negative number, prompt the user to enter a valid input
    if not num_of_disks.isdigit() or int(num_of_disks) <= 0:
        print("Invalid entry, please enter an integer number greater than zero.")
        continue
    else:
        # Convert the user's input into an integer, as the input itself is a string by default
        num_of_disks = int(num_of_disks)
        break

# Prompt the user to enter the name of the starting peg
peg_start = input("Enter the name of the starting peg\n")

# Prompt the user to enter the name of the destination peg
peg_dest = input("Enter the name of the destination peg\n")

# Prompt the user to enter the name of the auxiliary peg
peg_aux = input("Enter the name of the auxiliary peg\n")

# Run the algorithm that solves the Hanoi Towers problem, using the user's input
hanoi_towers(num_of_disks, peg_start, peg_dest, peg_aux)

# In the end, prompt the user to press Enter, in order to exit the program
input("Press Enter to exit the program")