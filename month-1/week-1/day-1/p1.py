productCost=int(input("Enter The Product cost: "))
discountRate=int(input("Enter The Discount Rate: "))

discount= productCost*discountRate/100

final_price=productCost-discount

print(f"Total Price :{final_price:.2f}")

