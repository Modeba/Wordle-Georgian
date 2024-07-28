def check_guess(answer, guess):
    # Convert both to lists
    saved_answer = answer
    guess, answer = list(guess), list(answer)
    notFound = set()

    for i in range(len(guess)):
        
        # Validate if the character is present in the answer
        if guess[i] not in saved_answer:
            notFound.add(guess[i])
            guess[i] = 'B'
            continue

        # Character is in the correct position
        if guess[i] == answer[i]:
            guess[i] = 'G'
            answer[i] = None
            continue
        
        # Character is in the answer but incorrect position
        for j in range(len(answer)):
            if guess[i] == answer[j]:
                guess[i] = 'Y'
                answer[j] = None
                break

    return guess, notFound


print(check_guess('smock', 'plane'))