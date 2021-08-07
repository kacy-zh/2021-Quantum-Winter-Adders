def list_to_num(bin_list):
    """ Turns the binary list to a number """
    
    result = 0
    for i in bin_list:
        result = (result << 1) | i
    return result

def to_binary(num, length):
    """ Turns a number into a list of its binary representation """
    
    format_string = "{0:0" + str(length) + "b}"
    return [int(x) for x in list(format_string.format(num))]


def find_addition(number):
    """ Finds b2b1b0 <- a2a1a0 + b2b1b0 in a binary number of length 6 """
    
    # Separate the two numbers
    binary =  [int(x) for x in list('{0:06b}'.format(number))]
    first = binary[:3]
    second = binary[3:]
    first.reverse()
    second.reverse()
    
    # Add the numbers
    bin_sum = list_to_num(first) + list_to_num(second)
    binary =  [int(x) for x in list('{0:06b}'.format(bin_sum))]
    binary = binary[3:]
    
    # Reverse the numbers appropriately
    first.reverse()
    binary.reverse()
    first.extend(binary)
    return list_to_num(first)

def get_qubits(input_number, length):
    """ Get the list of qubits in states from the binary representation for use in Qiskit
    
    Args:
        input_number: The input number
        length: Total length """
    
    format_string = "{0:0" + str(length) + "b}"
    binary = [int(x) for x in list(format_string.format(input_number))]
    qubits = []
    for q in range(length):
        if binary[length-q-1] == 1:
            qubits.append(q)
    return qubits