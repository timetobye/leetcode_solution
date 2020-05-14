class Solution:
    def reverse(self, number):
        sign = 1

        if number < 0:
            number *= -1
            sign = -1

        str_numbers = str(number)
        reversed_str_numbers = reversed(str_numbers)

        number_list = []
        for idx, str_number in enumerate(reversed_str_numbers):
            if str_number == 0 and idx == 0:
                continue

            number_list.append(str_number)

        reversed_result = int(''.join(number_list)) * sign

        if reversed_result >= 2147483647 or reversed_result <= -2147483648:

            return 0

        return reversed_result






