Check_the_word = input("what word you want to check for palindrome?: ").strip().lower()
if Check_the_word == Check_the_word[::-1]:
    print("yes it is a palindrome!!")
else:
    print("Opps!! It is not a palindrome. Try with different word.")
