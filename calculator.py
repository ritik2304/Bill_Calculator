def calculate_bill(price, discount, gst):
    discount_amount = (price * discount) / 100
    price_after_discount = price - discount_amount

    gst_amount = (price_after_discount * gst) / 100
    final_amount = price_after_discount + gst_amount

    return final_amount


price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))
gst = float(input("Enter GST percentage: "))

final_bill = calculate_bill(price, discount, gst)

print(f"\nFinal Bill Amount: ₹{final_bill:.2f}")