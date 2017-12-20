from decimal import Decimal

#print welcome header
print("-------- Annuitätischer Darlehensrechner --------")
print("-----------------Version 1.0.0 ------------------")
print("--------------- by David Lingmann ---------------")

#input required values as string
loan_amount_str = input("Kreditbetrag:")
interest_rate_str = input("Zinssatz:")
years_str = input("Jahre:")

#initialzing required variables
loan_amount = 0
interest_rate = 0
years = 0

#try conversion from string to decimal
try:
    loan_amount = Decimal(loan_amount_str)
except Exception as ex:
    print("Der Eingegeben Kreditbetrag ist keine gültige Zahl.")
    exit()

try:
    interest_rate = Decimal(interest_rate_str)
except Exception as ex:
    print("Der Eingegeben Zinssatz ist keine gültige Zahl.")
    exit()

try:
    years = int(years_str)
except Exception as ex:
    print("Der Eingegebenen Jahre sind keine gültige Zahl.")
    exit()

#check input values
if(loan_amount <= 0):
    print("Der Kreditbetrag muss größer 0 sein.")
    exit()

if(interest_rate <= 0 or interest_rate > 10):
    print("Der Zinssatz muss größer 0 sein und in einem sinnvollem Bereich liegen (bis 10%)")
    exit()

if(years <= 0 or years > 80):
    print("Die Anzahl der Jahre muss größer als 0 sein und in einem sinnvollem Bereich liegen (bis 80 Jahre)")

#convert percent value to decimal value (e.g. 4% -> 0.04)
interest_rate_decimal = (interest_rate / 100)

print("Berechnung läuft...")

#calculate interest cost value. Source: https://www.zinsen-berechnen.de
interest_cost = loan_amount * ((((interest_rate_decimal + 1) ** years) * interest_rate_decimal) / (((interest_rate_decimal + 1) ** years) - 1))

print("Annuitätendarlehen wurde erfolgreich berechnet")
print("Zinskosten:" + str(round(interest_cost, 2)).replace(".", ",") + "€")
print("Annuität:" + str(round(interest_cost + loan_amount, 2)).replace(".", ",") + "€")

print("Das Programm wird beendet")

