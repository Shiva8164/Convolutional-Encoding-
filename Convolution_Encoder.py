
import streamlit as st 
def encoded(memory): 
    x1 = memory[0] ^ memory[1] ^ memory[2] 
    x2 = memory[0] ^ memory[2] 
    encode = [x1, x2] 
    return encode 
def main(): 
    st.title("Convolutional Code Encoder") 
    binary_input = st.text_input("Enter the binary data (e.g., 101010):") 
    if st.button("Encode"): 
        encoded_bits = convolutional_encode(binary_input) 
        st.write("Encoded Bits:", encoded_bits) 
def convolutional_encode(binary_input): 
    memory = [0, 0, 0] 
    encoded_bits = [] 
    while binary_input: 
        memory[0] = int(binary_input[-1]) 
        encoded_bits.append(encoded(memory)) 
        memory[2], memory[1], memory[0] = memory[1], memory[0], 0 
        binary_input = binary_input[:-1] 
    while memory != [0, 0, 0]: 
        encoded_bits.append(encoded(memory)) 
        memory[2], memory[1], memory[0] = memory[1], memory[0], 0 
    array_strings = ["".join(map(str, array)) for array in encoded_bits] 
    result_string = "".join(array_strings) 
    return result_string 
 
if __name__ == "__main__": 
    main() 