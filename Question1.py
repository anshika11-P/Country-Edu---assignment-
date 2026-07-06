# Question 1- convert integer into english word

ones = ["", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine"]

teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
         "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


# Converts numbers from 1 to 999
def convert(num):
    words = ""
    if num >= 100:
        words += ones[num // 100] + " Hundred "
        num %= 100
    if 10 <= num <= 19:
        words += teens[num - 10]
    else:
        if num >= 20:
            words += tens[num // 10] + " "
            num %= 10
        if num > 0:
            words += ones[num]
    return words.strip()

# Main function
def number_to_words(num):

    if num == 0:
        return "Zero"
    if num < 0:
        return "Negative " + number_to_words(-num)
    result = ""

    crore = num // 10000000
    num %= 10000000
    lakh = num // 100000
    num %= 100000
    thousand = num // 1000
    num %= 1000
    hundred = num

    if crore:
        result += convert(crore) + " Crore "
    if lakh:
        result += convert(lakh) + " Lakh "
    if thousand:
        result += convert(thousand) + " Thousand "
    if hundred:
        result += convert(hundred)
    return result.strip()


# Take input from user
number = int(input("Enter an integer: "))

# Print answer
print("In English:", number_to_words(number))