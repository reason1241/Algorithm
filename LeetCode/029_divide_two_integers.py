# Work well but not acceptable
# Because the constraint of the problem is "Do not use multiplication, division.".
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         result =  int(dividend / divisor)
        
#         if result > (2 ** 31 - 1):
#             return 2 ** 31 - 1
        
#         if result < -(2 ** 31):
#             return -(2 ** 31)

#         return result


# Cast int to str and calculate numbers as a human does.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_pos = ((dividend > 0) == (divisor > 0))
        
        abs_divisor, abs_dividend = abs(divisor), abs(dividend)
        
        quotient = ""
        current_cal = ""
    
        str_dividend = str(abs_dividend)
    
        for i in range(len(str_dividend)):
            current_cal += str_dividend[i]
            
            if int(current_cal) < abs_divisor:
                quotient += "0"
                continue
            
            partial_quotient = 0
            
            while int(current_cal) >= abs_divisor:
                current_cal = str(int(current_cal) - abs_divisor)
                partial_quotient += 1
            
            quotient = quotient + str(partial_quotient)
                
        if is_pos:
            return min(int(quotient), 2 ** 31 - 1)
        
        return int(f"-{quotient}")


# Use shift operator
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         is_pos = ((dividend > 0) == (divisor > 0))
#         abs_divisor, abs_dividend = abs(divisor), abs(dividend)
        
#         quotient = 0
        
#         while abs_dividend >= abs_divisor:
#             total, partial_quotient = abs_divisor, 1
            
#             while (total << 1) <= abs_dividend:
#                 total <<= 1
#                 partial_quotient <<= 1
                
#             quotient += partial_quotient
#             abs_dividend -= total
        
#         if is_pos:
#             return min(quotient, (2 ** 31) - 1)
        
#         return max(-quotient, -2**31)
        