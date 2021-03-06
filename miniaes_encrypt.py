'''
Here is where the magic encryption happens!
:author: Lena Heimberger
:date: 31-07-2017
'''
from miniaes_functions import *

nibble_size = 4  # a nibble is four bits
const_column=nibbles_to_bits(['0011','1010','1010','0011']) #d0= 3, d1=2, d2=2, d3=3

def mix_column(string):
    '''
    Implements MixColumn
    arg0: the subbed and shifted string
    xors each string nibble with the corresponding constant
    column nibble, which is defined in the paper by Chung)
    return: the mix_colum result string
    '''
    bits=nibbles_to_bits(string)
    res=[]
    bit=nibbles_to_bits(string)
    for i in range(0, len(bits)):
        res.append(string_bitwise_xor(bit[i], const_column[i%nibble_size]))
    return res


def shift_row(substring):
    '''
        Implements ShiftRow
        The third and the first bit of a nibble
        are exchanged
        arg0: substring: the already nibble_subbed
        return: the shifted string
    '''
    new_string = []
    for i in range(len(substring)):
        tmp_str = ''
        tmp_str += substring[i][0]
        tmp_str += substring[i][3]
        tmp_str += substring[i][2]
        tmp_str += substring[i][1]
        ''.join(tmp_str)
        new_string.append(tmp_str)
    return new_string

def nibble_sub(nibblestr):
    '''
        This acts as an S Box in mini AES
        arg0: the string of arguments
        return: a substituation string
    '''
    substitute = []
    for i in range(len(nibblestr)):
        if nibblestr[i] == '0000':
            substitute.append('1110')
        elif nibblestr[i] == '0001':
            substitute.append('0100')
        elif nibblestr[i] == '0010':
            substitute.append('1101')
        elif nibblestr[i] == '0011':
            substitute.append('0001')
        elif nibblestr[i] == '0100':
            substitute.append('0010')
        elif nibblestr[i] == '0101':
            substitute.append('1111')
        elif nibblestr[i] == '0110':
            substitute.append('1011')
        elif nibblestr[i] == '0111':
            substitute.append('1000')
        elif nibblestr[i] == '1000':
            substitute.append('0011')
        elif nibblestr[i] == '1001':
            substitute.append('1010')
        elif nibblestr[i] == '1010':
            substitute.append('0110')
        elif nibblestr[i] == '1011':
            substitute.append('1100')
        elif nibblestr[i] == '1100':
            substitute.append('0101')
        elif nibblestr[i] == '1101':
            substitute.append('1001')
        elif nibblestr[i] == '1110':
            substitute.append('0000')
        elif nibblestr[i] == '1111':
            substitute.append('0111')
    return substitute

def key_addition(step_3): 
    print(step_3)
    return step_3 


def matrix_nibble_generator(plaintext):
    # get bits
    bitstring = string_to_binary(plaintext)
    # turn them in a matrix
    nibblestr = generate_matrix(bitstring)
    # nibble sub function
    step_1 = nibble_sub(nibblestr)
    # shift row
    step_2 = shift_row(step_1)
    # mix column
    step_3 = mix_column(step_2)
    # key addition
    step_4 = key_addition(step_3)

matrix_nibble_generator('Lena')
# for testing
