seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
overstock_risk= seasonal and (current_stock>high_stock_threshold)
make_discount= overstock_risk or discount_eligible
discount_eligible=not(selling_well and not(on_sale))
print ("Should the item be discounted? "+str(make_discount))