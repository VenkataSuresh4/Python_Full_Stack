alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

want_continue = False


def encrypt(value, number):
    new_word = []
    for letter in text:
        current_index = alphabet.index(letter)
        new_word.append(alphabet[current_index + shift])

    output_text = ""
    for word in new_word:
        output_text += word

    print(output_text)


def decrypt(value, number):
    new_word = []
    for letter in text:
        current_index = alphabet.index(letter)
        new_word.append(alphabet[current_index - shift])

    output_text = ""
    for word in new_word:
        output_text += word

    print(output_text)


while not want_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    do_it_again = input("Do you want to continue [Yes or No] ")
    if do_it_again == 'No':
        want_continue = True
