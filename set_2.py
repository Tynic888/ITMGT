def shift_letter(letter, shift):
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    location = Alphabet.find(letter)
    final_location = location + shift - 1
    alphabet_length = int((final_location+1)/26) 

    if location + shift >= 26:
        final_location = location + shift - 26*alphabet_length -1

    shifted_letter = Alphabet[final_location+1]

    if letter.isalpha()==False:
        shifted_letter = " "

    return shifted_letter
    
def caesar_cipher(message, shift):
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = 0
    letter_count = len(message) - 1 
    
    new_message = ""

    while letter <= letter_count:
        current_letter = message[letter]
        current_location = Alphabet.find(current_letter)
        current_shift = current_location + shift 
        alphabet_length = int((current_shift)/26) 
        if current_shift >= 26:
            current_shift = current_location + shift -26*alphabet_length 
            shifted_letter = Alphabet[current_shift]



        else:
            shifted_letter = Alphabet[current_shift]
        
        if current_letter.isalpha()==False:
            shifted_letter = " "


        letter = letter + 1
        new_message = new_message + shifted_letter


    return new_message

def shift_by_letter(letter, letter_shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    location_letter = alphabet.find(letter)
    location_shift = alphabet.find(letter_shift)
    new_location = location_letter + location_shift
    alphabet_length = int((new_location)/26)
    

    new_location = location_letter + location_shift - 26*alphabet_length
    new_letter = alphabet[new_location]

    if letter.isalpha()==False:
        new_letter = " "
   
    return new_letter

def vigenere_cipher(message,key):
        key_index = 0
        vigenere_text = ""

        for i in message:
            vigenere_text += shift_by_letter(i, key[key_index % len(key)])
            key_index += 1
        return vigenere_text
        
def scytale_cipher(message,shift):
    while len(message) % shift != 0:
        message += '_'
        
    scytale_text = ''
    for i in range(len(message)):
        scytale_text += message [(i // shift) + (len(message) // shift) * (i % shift)]
    return scytale_text

def scytale_decipher(message,shift):
    decoded_text = ''

    for i in range(len(message)):
        decoded_text += message[(i % (len(message) // shift)) * shift + (i // (len(message) // shift))]
    return decoded_text 