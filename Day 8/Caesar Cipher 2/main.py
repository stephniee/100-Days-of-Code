alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(where_to,original_text,shift_amount):
    # Angela's solution
    output_text = ""
    if where_to == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {where_to}d result: {output_text}")

    # my own messy solution
    # if where_to == "decode":
    #     decrypted_string = ""
    #     # TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
    #     # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
    #     #  by the shift amount and print the decrypted text.
    #     for letter in original_text:
    #         if letter in alphabet:
    #             pos = alphabet.index(letter) + (shift_amount * -1)
    #             decrypted_string += alphabet[pos]
    #     print(decrypted_string)
    # if where_to == "encode":
    #     cipher_text = ""
    #     for letter in original_text:
    #         if letter in alphabet:
    #             shifted_position = alphabet.index(letter) + shift_amount
    #             shifted_position %= len(alphabet)
    #             cipher_text += alphabet[shifted_position]
    #     print(f"Here is the encoded result: {cipher_text}")



caesar(where_to=direction,original_text=text,shift_amount=shift)

