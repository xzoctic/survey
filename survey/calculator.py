import math

class Calculator:

    def calculate_term(self, principal, interest_rate, monthly_payment):
        #return -(math.log(1-(interest_rate*principal)/monthly_payment))/math.log(1+interest_rate)
        print((interest_rate*principal)/monthly_payment)
        numerator = -math.log(1-(interest_rate*principal)/monthly_payment)
        denominator = math.log(1+interest_rate)
        return numerator/denominator

    def calculate_monthly_payment(self, principal, interest_rate, months):

        numerator = interest_rate*principal
        denominator = 1-((1+interest_rate)**(-months))

        return numerator/denominator

