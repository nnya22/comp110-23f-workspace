"""Exercise 2 - One Shot Wordle."""
__author__ = "730324119"

secret_word: str = "python"
length: int = len(secret_word)
guess: str = input(f"What is your {length}-letter guess? ")

# emoji variables!
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# if guess was out of bounds, let them know and ask for a different guess
while len(guess) != len(secret_word):
    guess = str(input((f"That was not {length} letters! Try again: ")))
# we need to check if each index of the guess matches the corresponding index of the secret_word

i_a: int = 0
emoji_string: str = ""

# checks letter by letter within the guess to assess wether it is true and should be a green box, yellow box or white box
while i_a < len(secret_word):
    character_exists_in_secret: bool = False    
    
    i_b: int = 0
    # for a single letter of the guess (guess[i_a], determine if that letter exists in any position of secret_word)
    while i_b < len(secret_word):
        if (secret_word[i_b] == guess[i_a]):
            character_exists_in_secret = True
        i_b = i_b + 1
    
    # if the letter at position i_a is equal in both the secret word and the guess, add a green box to the emoji string.
    if (secret_word[i_a] == guess[i_a]):
        emoji_string = emoji_string + GREEN_BOX
    # Else, if that letter exists somewhere else in the secret_word add a yellow box.
    elif (character_exists_in_secret is True ):
        emoji_string = emoji_string + YELLOW_BOX
    # If neither is true add a white box.
    else:
        emoji_string = emoji_string + WHITE_BOX

    i_a = i_a + 1 

print(emoji_string)

# if guess matches the length of the secret word, but is not right tell them
if (guess != secret_word):
    print("Not quite. Play again soon!")
        
else:
    # if you've reached this point guess == secret
    print("Woo! You got it!")