import numpy as np

def print_matrix(m):
    """ Given a matrix, prints it out """
    for row in m:
        for cell in row:
            print(cell," ",end="")
        print()
        
def identity_matrix(w):
    """ Creates the identity matrix of size w """
    m = [[0 for x in range(w)] for y in range(w)] 
    for i in range(w):
        m[i][i] = 1
    return m

def step_matrix(iden_start, ccnot, iden_end):
    """ Produces I (x) ccnot (x) I
    
    Args:
        iden_start: Number of I at the start
        ccnot: A gate in matrix form
        iden_end: Number of I at the end
    """
    start = identity_matrix(pow(2,iden_start))
    final = np.kron(start, ccnot)
    end = identity_matrix(pow(2,iden_end))
    return np.kron(final, end)

def cnot(controls, target):
    """ Produces the c(c)not gate with the specified controls and target
    
    Args:
        controls (list): Control qubits, numbered starting 1
        target: Target qubit, numbered starting 1
    """
    # Find the maximum number
    if len(controls) > 0:
        maximum = max(controls)
    else:
        maximum = target

    if target > maximum:
        maximum = target

    # Find the missing values
    missing = [1] * (maximum)
    missing[target-1] = 0

    # Keep a sum of the constant values
    constant_val = 0

    # Find not missing and update constant_vals
    for i in controls:
        missing[i-1] = 0   
        constant_val += pow(2,maximum-i)

    # If there is a missing number then update its value
    for i in range(len(missing)):
        if missing[i] == 1:
            missing[i] = pow(2,maximum-i-1)

    # Truncate 0s
    missing = [i for i in missing if i != 0]  

    # Permute sum calculates what pairs get swapped
    target_val = pow(2,maximum-target)
    permute_sum = permute_sums(None, missing)
    for i in range(len(permute_sum)):
        permute_sum[i] = [constant_val + permute_sum[i], constant_val + permute_sum[i] + target_val]

    # Creates the matrix
    matrix_length = pow(2,maximum)
    matrix = identity_matrix(matrix_length)

    # Make necessary changes to the cnot matrix
    for pairs in permute_sum:
        i = pairs[0]
        j = pairs[1]
        matrix[i][i] = 0
        matrix[j][j] = 0
        matrix[i][j] = 1
        matrix[j][i] = 1

    return matrix

def permute_sums(answer, current_list):
    """ Permutes the sums of all numbers in current_list with each other
    
    Args:
        answer: This is a recursive function, answer stores the answer
        current_list: The list to permute
    """
    # If no list given just return 0
    if len(current_list) == 0:
        return [0]

    # If at start then start of list
    elif answer is None:
        answer = [0, current_list[0]]

    # Add 0 and current_list[0] to all entries
    else:
        add = answer[:]
        for i in range(len(add)):
            add[i] += current_list[0]
        answer.extend(add)

    # If last, just return answer
    if len(current_list) == 1:
        return answer

    # If not last, continue and remove one from the current list
    return permute_sums(answer, current_list[1:])

