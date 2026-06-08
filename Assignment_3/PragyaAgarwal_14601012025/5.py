def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

num = int(input("Enter a number: "))
palindrome(num)