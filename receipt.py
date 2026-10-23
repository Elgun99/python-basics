coffee = 4.50
cheesecake = 6.00
water = 1.00

total = coffee + cheesecake + water
vat = total * 0.18
final_total = total + vat

print("------ KAFE ------")
print(f"Kofe:       {coffee:.2f} AZN")
print(f"Çizkeyk:    {cheesecake:.2f} AZN")
print(f"Su:         {water:.2f} AZN")
print("------------------")
print(f"Cəmi:       {total:.2f} AZN")
print(f"ƏDV 18%:    {vat:.2f} AZN")
print(f"Yekun:      {final_total:.2f} AZN")