#Program 1 - INVOICE GENERATION

prods=int(input("How many products have you purchased? "))
print()
id_ls=[]
name_ls=[]
qty_ls=[]
price_ls=[]
dis_ls=[]
discount=0
total=0
bill=0

for loop in range(prods):
    pname=input(f"Enter the name of the product {loop+1}: ")
    pid='PDT-'+pname[0].upper()+str(loop)
    qty=int(input("Enter its quantity: "))
    price=float(input("Enter its price: "))

    if price>=200 and price<500:
        print("This product has a discount of 2 %")
        discount=price*2/100
    elif price>=500 and price<1000:
        print("This product has a discount of 5 %")
        discount=price*5/100
    elif price>=1000 and price<5000:
        print("This product has a discount of 8 %")
        discount=price*8/100
    elif price>=5000:
        print("This product has a discount of 10 %")
        discount=price*10/100
    else:
        discount=0

    name_ls.append(pname)
    id_ls.append(pid)
    qty_ls.append(qty)
    price_ls.append(price)
    dis_ls.append(discount)
    print()

print("\t\t\tFINAL INVOICE\n")    
print("Prod_ID\tProd_Name\tQty\tPrice\tDiscount\tTotal")
for loop in range(prods):
    total=price_ls[loop]*qty_ls[loop]-dis_ls[loop]
    print(f"{id_ls[loop]}\t{name_ls[loop]}\t\t{qty_ls[loop]}\t{price_ls[loop]}\t{dis_ls[loop]}\t{total}")
    bill=bill+total
print(f"\t\t\t\tBILL AMOUNT:\t{bill}")

    

        
