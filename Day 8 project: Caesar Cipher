alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        if char not in alphabet:
          end_text += char
        else:
          position = alphabet.index(char)
          new_position = (position + shift_amount) % 26
          end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")
    
import art
print(art.logo)

restart=True
while restart:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if go_again =="no":
    restart = False
    print("Goodbye")
