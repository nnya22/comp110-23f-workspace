"""Exercise 03, Structure Wordle"""
author: str = "730324119"

# emoji variables!
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(secret_word: str, single_letter: str) -> bool:
    """When given two strings it will return True if the single letter is found at any index of the secret word"""
    assert len(single_letter) == 1
    # checks letter by letter within the guess to assess wether it is true and should be a green box, yellow box or white box
    i_a: int = 0
    emoji_string: str = ""
    while i_a < len(secret_word):
        single_letter_exists_in_secret: bool = False    

        i_b: int = 0
        # for a single letter of the guess (guess[i_a], determine if that letter exists in any position of secret_word)
        while i_b < len(secret_word):
            if (secret_word[i_b] == single_letter[i_a]):
                return True
            i_b = i_b + 1
        
        # if the letter at position i_a is equal in both the secret word and single letter, add a green box to the emoji string.
        if (secret_word[i_a] == single_letter[i_a]):
             emoji_string = emoji_string + GREEN_BOX
        # Else, if that letter exists somewhere else in the secret_word add a yellow box.
        elif (single_letter_exists_in_secret is True):
            emoji_string = emoji_string + YELLOW_BOX
        # If neither is true add a white box.
        else:
            emoji_string = emoji_string + WHITE_BOX
            return False
        i_a = i_a + 1
    def emojified(guess: str, secret: str) -> str:
        """Given two strings, equal in length, the first a guess and the second a secret, this function will return a specific string of emoji"""
        assert len(guess) == len(secret)        
        checker: str = contains_char(guess, secret)
        print(checker)