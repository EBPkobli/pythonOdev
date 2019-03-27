import sqlite3;
d0 = sqlite3.connect('ders/sql/Firm.db');
c0 = d0.cursor();
#a0 = c0.execute("Select * from Customer where Country = 'Germany' or Country = 'UK' or Country='France'").fetchall();


#birim fiyatı 10 dolar ile 20 dolar arasında olan (dahil) ürünleri satın aldığın tedarikçilerin
#firma adı şehri ülkesi ve telefonu listelenecek.
a0 = c0.execute("Select Supplier.CompanyName, Supplier.Country, Supplier.Phone from Product left join Supplier on Product.SupplierId = Supplier.Id Where UnitPrice Between 10 and 20").fetchall();

for a00 in a0:
    print(a00[0][:25] + ' ' * (35-len(a00[0][:25])) + a00[1][:15] + ' ' *(18-len(a00[1][:15])) + a00[2][:15] + ' ' * (18-len(a00[2][:15])))

print("-------------------")

#en çok sattığım 10 ürünün ürün adı hangi ülkelere satılıyo ve bu ülkere bugüne kadar kaçar tane satılmış rapor hazırlanacak
sqlStr = "Select Product.ProductName, Customer.Country, OrderItem.Quantity from OrderItem "
sqlStr = sqlStr + "left join Product on OrderItem.ProductId = Product.Id "
sqlStr = sqlStr + "left join 'Order' on OrderItem.OrderId = 'Order'.Id " 
sqlStr = sqlStr + "left join Customer on 'Order'.CustomerId = Customer.Id "
sqlStr = sqlStr + "order by OrderItem.Quantity desc limit 10"
a1 = c0.execute(sqlStr).fetchall()

for a11 in a1:
    print(a11[0] + ' ' * (50 - len(a11[0])) + a11[1] + ' ' * (18 - len(a11[1])) + str(a11[2]))


print("-------------------")
#ürün aldığım tüm ülkeleri yaptığım cirolarla beraber raporlayalım. mesala amerikadan şunu alıyorum alım ciroları x ürününden 1000 tane satmışım nereden almışım ona bakıcam 

sqlStr_countries = "Select Distinct Country from Supplier"
a2 = c0.execute(sqlStr_countries).fetchall()
for a22 in a2:
    sqlStr_sum = "select sum(OrderItem.UnitPrice* OrderItem.Quantity) from OrderItem "
    sqlStr_sum = sqlStr_sum + "left join Product on OrderItem.ProductId = Product.Id "
    sqlStr_sum = sqlStr_sum + "left join Supplier on Product.SupplierId = Supplier.Id "
    sqlStr_sum = sqlStr_sum + "where Supplier.Country = '"+ a22[0] +"'"
    a3 = c0.execute(sqlStr_sum).fetchall()
    print(a22[0] + ' ' * (40-len(a22[0])) + str(a3[0][0]))

print("-------------------")



#ürün sattığım ülkeye yaptığım ciro..

sqlStr_countries = "Select Distinct Country from Customer"
a4 = c0.execute(sqlStr_countries).fetchall()
for a44 in a4:
    sqlStr_sum = "select sum(OrderItem.UnitPrice* OrderItem.Quantity) from OrderItem "
    sqlStr_sum = sqlStr_sum + "left join 'Order' on OrderItem.OrderId = 'Order'.Id "
    sqlStr_sum = sqlStr_sum + "left join Customer on 'Order'.CustomerId = Customer.Id "
    sqlStr_sum = sqlStr_sum + "where Customer.Country = '"+ a44[0] +"'"
    a5 = c0.execute(sqlStr_sum).fetchall()
    print(a44[0] + ' ' * (40-len(a44[0])) + str(a5[0][0]))