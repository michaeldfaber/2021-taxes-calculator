import string

taxableIncome = 0
taxes = 0

def calculateTaxes():
    print("\nWhat is your gross annual income?\n")
    grossAnnualString = raw_input().replace("$", "").replace(",", "")
    grossAnnual = int(grossAnnualString)

    if grossAnnual < 12550:
        print("\nYour income is below the 2021 standard deduction. You will not pay federal taxes.\n")
        return

    global taxableIncome
    taxableIncome = grossAnnual - 12550
    calculateTaxesForBracket(523600, 0.37)
    calculateTaxesForBracket(209425, 0.35)
    calculateTaxesForBracket(164925, 0.32)
    calculateTaxesForBracket(86375, 0.24)
    calculateTaxesForBracket(40525, 0.22)
    calculateTaxesForBracket(9950, 0.12)
    calculateTaxesForBracket(0, 0.10)
    
    print("\nIncome after Federal Income Taxes: $" + str(grossAnnual - taxes))
    print("\nFederal Income Taxes Paid: $" + str(taxes))
    print("\nDisclaimer: This calculator assumes you're single with no dependents, among other things. There's a lot of caveats when it comes to taxes. It might not be wise to make serious decisions based on these results. For more on this, and to see where I found these numbers, read here: https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2021")
    
    
# bracketPercentage as a decimal (0.35 = 35%)
def calculateTaxesForBracket(bracketMinimum, bracketPercentage):
    global taxableIncome
    global taxes
    if taxableIncome > bracketMinimum:
        taxedInThisBracket = taxableIncome - bracketMinimum
        taxes += taxedInThisBracket * bracketPercentage
        taxableIncome -= taxedInThisBracket
    
calculateTaxes()