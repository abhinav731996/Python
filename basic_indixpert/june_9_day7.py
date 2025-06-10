# for n in range(1,11):
#     print(n)

# **************************************
# for n in range(1,11):
#     print("2 *",n,"=", 2*n)


# **************************************
# for n in range (1,51):
#     for m in range (1,11):
#         print(f"{n}*{m}={n*m}")
    
#     print("*"*8)



# **************************************list data

# listdata = [10,20,30,80,90,40,50]
# listdata = ["abhinav", "kailash","denish","aditya"]

# # num = int(input("enter number: "))
# name = (input("enter name: "))

# for item in listdata:
#     if item.lower() == name.lower():
#         print("number exist")
    

# **************************************dictionary data

# dicdata = {"id":101, "name":"Abhinav", "Address":"Rohtak"}

# for keys,values in dicdata.items():

# for keys,values in dicdata:
#     print(keys,values)



# **************************************dictionary data

dicdata = [{"id":101, "name":"Abhinav", "Address":"Rohtak"},
           {"id":102, "name":"Abhinav", "Address":"Rohtak"}
           ]
for item in dicdata:
    for keys,values in item.items():
        print(keys,"=", values)
    