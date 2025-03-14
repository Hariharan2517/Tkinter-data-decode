import tkinter as tk
from tkinter import ttk
#from threading import Timer
from tkinter import *

#value = 3039606303C86A4056BB34CF
import math

#Using hexdeci() for converting Hex => Binary => Decimal format
def hexdeci():
  global sum_value, sum_val, value, decimal3_str
  #getting entry value from tk
  ini_string = hex_entry.get()
  scale = 16

  # Printing initial string
  print ("Initial string", ini_string)

  # Code to convert hex to binary and replace 'b' with '0'
  res = bin(int(ini_string, scale)).zfill(8).replace('b', '0')

  #Print the resultant string hex to binary
  #INSERT Method for inserting value in Tkinter
  print(res,"int")
  print ("Resultant string", str(res))
  #inserted Binary in entry
  binary_entry.insert("1",res)  
  print(len(res))

  #Using slice method upto the value
  #Header - 8bit
  header = slice(0, 8)
  print(res[header],"header 8")
  print(len(res[header]))
  #inserted header value in tk
  partition1_entry.insert("1",res[header]) 

  #Filter - 3bit
  filter = slice(8,11)
  print(res[filter],"filter 3")
  print(len(res[filter]))
  #inserted filter value in tk
  partition2_entry.insert("1",res[filter])

  #Partition - 3bit
  partition = slice(11,14)
  print(res[partition],"partition 3")
  print(len(res[partition]))
  #inserted partition value in tk
  partition3_entry.insert("1",res[partition])

  #GS1 comapny - 20bit
  gs1_comapny = slice(14,34)
  print(res[gs1_comapny],"gs1_comapny 20")
  data1 = res[gs1_comapny]
  print(len(res[gs1_comapny]))
  #inserted gs1 value in tk
  partition4_entry.insert("1",data1)

  #Item - 24bit
  item = slice(34,58)
  print(res[item],"item 24")
  data2 = res[item]
  print(len(res[item]))
  #inserted item value in tk
  partition5_entry.insert("1",data2)

  #Serial no - 38bit or greater
  serial_no = slice(58,len(res))
  print(res[serial_no],"Serial no 38")
  data3 = res[serial_no]
  print(len(res[serial_no]))
  print(type(data3))
  #inserted Serial value in tk
  partition6_entry.insert("1",data3)


  binary1 = data1
  decimal1 = int(binary1, 2)#binary to decimal
  decimal1_str = str(decimal1)
  print(decimal1,"GS1 company")
  print(decimal1_str.rjust(6, "0"),"if less than 6 digit add 0") # Adding 0 before upto 6 digit
  gs1_entry.insert("1", decimal1_str.rjust(6, "0"))


  binary2 = data2
  decimal2 = int(binary2, 2)
  print(decimal2,"Item")
  decimal2_str = str(decimal2) 
  print(len(decimal2_str))

  binary3 = data3
  decimal3 = int(binary3, 2)
  print(decimal3,"Serial no") 
  decimal3_str = str(decimal3)
  print(len(decimal3_str))
  serialno_entry.insert("1", decimal3_str)

#If Item is less than 7 digit 
  if len(decimal2_str) < 7:
    print("This func() has lesser than 7 digit")
    data2_str = decimal2_str.rjust(7, "0")
    deci_str = decimal1_str.rjust(6, "0")
    item_entry.insert("1", data2_str)
    print(len(data2_str))
    print(data2_str,"Adding 0 for 7bit")
    print(data2_str)
    adding_data = deci_str+"."+data2_str+"."+decimal3_str
    print(adding_data,"Added data")
    new_adding_data = data2_str[0]+deci_str+data2_str[1:7]+"."+decimal3_str
    print(new_adding_data,"New added data Concatenate value")
    concatenate_entry.insert("1", new_adding_data)
    x = slice(13)
    value = new_adding_data[x]
    print(len(value))
    v1 = (int(value[0])*3)
    v2 = (int(value[1])*1)
    v3 = (int(value[2])*3)
    v4 = (int(value[3])*1)
    v5 = (int(value[4])*3)
    v6 = (int(value[5])*1)
    v7 = (int(value[6])*3)
    v8 = (int(value[7])*1)
    v9 = (int(value[8])*3)
    v10 = (int(value[9])*1)
    v11 = (int(value[10])*3)
    v12 = (int(value[11])*1)
    v13 = (int(value[12])*3)
    print(len(value[0]))
    print(value,"split")
    sum_value = math.fsum([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13])
    sum_val = int(sum_value)
    checksum_entry.insert("1", sum_val)
    print(sum_value)
    

#If Item is equal to 7 digit 
  if len(decimal2_str) == 7:
    print("This func() has 7 digit")
    deci_str = decimal1_str.rjust(6, "0")
    add_data = deci_str+"."+decimal2_str+"."+decimal3_str
    item_entry.insert("1", decimal2_str)
    print(add_data,"Added data")
    new_add_data = decimal2_str[0]+deci_str+decimal2_str[1:7]+"."+decimal3_str
    print(new_add_data,"New added data Concatenate value")
    concatenate_entry.insert("1", new_add_data)
    x = slice(13)
    value = new_add_data[x]
    print(len(value))
    v1 = (int(value[0])*3)
    v2 = (int(value[1])*1)
    v3 = (int(value[2])*3)
    v4 = (int(value[3])*1)
    v5 = (int(value[4])*3)
    v6 = (int(value[5])*1)
    v7 = (int(value[6])*3)
    v8 = (int(value[7])*1)
    v9 = (int(value[8])*3)
    v10 = (int(value[9])*1)
    v11 = (int(value[10])*3)
    v12 = (int(value[11])*1)
    v13 = (int(value[12])*3)
    print(v2)
    print(len(value[0]))
    print(value,"split")
    sum_value = math.fsum([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13])
    sum_val = int(sum_value)
    checksum_entry.insert("1", sum_val)
    print(sum_val)

#Subtract func() for subtracting the check sum value
def subtract():
  print(sum_value)
  roundoff_value = subtract_entry.get()
  print(roundoff_value)
  valuess = (int(roundoff_value) - (sum_val))
  valuess_str = str(valuess)
  print(valuess,"Check sum")  
  finall_tag = "(01)"+value+valuess_str+"(21)"+decimal3_str.rjust(12, "0")
  print(finall_tag,"Final Tag ID")
  finaltag_entry.insert("1", finall_tag)
  
#Clear func() for clearing input field
def clear():
  hex_entry.delete(0, 200)
  binary_entry.delete(0, 200)
  partition1_entry.delete(0, 200)
  partition2_entry.delete(0,200)
  partition3_entry.delete(0,200)
  partition4_entry.delete(0,200)
  partition5_entry.delete(0,200)
  partition6_entry.delete(0,200)
  gs1_entry.delete(0,200)
  serialno_entry.delete(0,200)
  item_entry.delete(0,200)
  concatenate_entry.delete(0,200)
  checksum_entry.delete(0,200)
  finaltag_entry.delete(0,200)
  subtract_entry.delete(0,200)

# root window
root = tk.Tk()
root.geometry("590x620")
root.title('Data-decode')
root.resizable(610, 640)
# root background color
root.configure(bg='white')

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

title_label = ttk.Label(root, text="GS1 Standard data Decode",font=('Times', 22),background='white', foreground='black')
title_label.grid(column=1, row=0, sticky=tk.N, padx=10, pady=15,ipadx=20, ipady=0,columnspan=3)

# Hex
hex_label = ttk.Label(root, text="Hex value",font=('Times', 15),background='white', foreground='black')
hex_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=0,ipadx=17, ipady=0)

hex_entry = tk.Entry(root,font=('Normal', 16),background='DodgerBlue', foreground='white')
hex_entry.grid(column=1, row=1, sticky=tk.EW, padx=10, pady=5, columnspan=3,ipadx=2.5, ipady=0)
#username_entry.insert("1", "gawrge")

#convert button using command to call the func()
convert_button = tk.Button(root, text="convert",command= hexdeci,font=('Times', 12), background='white',foreground='blue')
convert_button.grid(column=2, row=2, sticky=tk.W, padx=5, pady=10)

#Binary
binary_label = ttk.Label(root, text="Binary",font=('Times', 16),background='white', foreground='black')
binary_label.grid(column=0, row=3, sticky=tk.W, padx=0, pady=10)

binary_entry = tk.Entry(root,font=('Normal', 12),background='DodgerBlue', foreground='white')
binary_entry.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=10,columnspan=3,ipadx=2.5, ipady=2.5)

#Partiton - 6 Inputs
partition_label = ttk.Label(root, text="Partition",font=('Times', 16),background='white', foreground='black')
partition_label.grid(column=0, row=4, sticky=tk.W, padx=0, pady=5)

partition1_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
partition1_entry.grid(column=1, row=4, sticky=tk.EW, padx=2, pady=2,ipadx=3, ipady=3)

partition2_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
partition2_entry.grid(column=2, row=4, sticky=tk.EW, padx=2, pady=2,ipadx=3, ipady=3)

partition3_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
partition3_entry.grid(column=3, row=4, sticky=tk.EW, padx=2, pady=2,ipadx=3, ipady=3)

partition4_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
partition4_entry.grid(column=1, row=5, sticky=tk.EW, padx=2, pady=2,ipadx=3, ipady=3)

partition5_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
partition5_entry.grid(column=2, row=5, sticky=tk.EW, padx=2, pady=2,ipadx=3, ipady=3)

partition6_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
partition6_entry.grid(column=3, row=5, sticky=tk.EW, padx=2, pady=2,ipadx=3, ipady=3)

#GS1- 6 Digit
gs1_label = ttk.Label(root, text="GS1-6",font=('Times', 16),background='white', foreground='black')
gs1_label.grid(column=0, row=6, sticky=tk.W, padx=0, pady=5,ipadx=10, ipady=0)

gs1_entry = tk.Entry(root,font=('Normal', 12),background='DodgerBlue', foreground='white')
gs1_entry.grid(column=1, row=6, sticky=tk.EW, padx=5, pady=5, columnspan=3,ipadx=2.5, ipady=2.5)

#Item – 7 Digit
item_label = ttk.Label(root, text="Item-7",font=('Times', 16),background='white', foreground='black')
item_label.grid(column=0, row=7, sticky=tk.W, padx=0, pady=5,ipadx=10, ipady=0)

item_entry = tk.Entry(root,font=('Normal', 12),background='DodgerBlue', foreground='white')
item_entry.grid(column=1, row=7, sticky=tk.EW, padx=5, pady=5, columnspan=3,ipadx=2.5, ipady=2.5)

#Serial No – 12 Digit
serialno_label = ttk.Label(root, text="Serial-no",font=('Times', 16),background='white', foreground='black')
serialno_label.grid(column=0, row=8, sticky=tk.W, padx=0, pady=0,ipadx=10, ipady=0)

serialno_entry = tk.Entry(root,font=('Normal', 12),background='DodgerBlue', foreground='white')
serialno_entry.grid(column=1, row=8, sticky=tk.EW, padx=5, pady=5, columnspan=3,ipadx=2.5, ipady=2.5)

#Concatenate
concatenate_label = ttk.Label(root, text="Concatenate",font=('Times', 14),background='white', foreground='black')
concatenate_label.grid(column=0, row=9, sticky=tk.W, padx=0, pady=15,ipadx=2.5, ipady=0)

concatenate_entry = tk.Entry(root,font=('Normal', 12),background='DodgerBlue', foreground='white')
concatenate_entry.grid(column=1, row=9, sticky=tk.EW, padx=5, pady=0, columnspan=3,ipadx=2.5, ipady=2.5)

#Check Sum value
checksum_label = ttk.Label(root, text="Check_sum",font=('Times', 14),background='white', foreground='black')
checksum_label.grid(column=0, row=10, sticky=tk.W, padx=0, pady=0,ipadx=10, ipady=0)

checksum_entry = tk.Entry(root,font=('Times', 14),background='DodgerBlue', foreground='red')
checksum_entry.grid(column=1, row=10, sticky=tk.E, padx=0, pady=0,ipadx=2.5, ipady=0)

#Subtract the check sum value to nearest equal 
subtract_label = ttk.Label(root, text="Subtract_value",font=('Times', 14),background='white', foreground='black')
subtract_label.grid(column=2, row=10, sticky=tk.E, padx=2, pady=5,ipadx=10, ipady=0)

subtract_entry = tk.Entry(root,font=('Times', 14),background='DodgerBlue', foreground='red')
subtract_entry.grid(column=3, row=10,  sticky=tk.EW, padx=2, pady=2,ipadx=3, ipady=3)

#subtract using command to call the subtract()
subtract_button = tk.Button(root, text="calculate",font=('Times', 12),command=subtract, background='white',foreground='blue')
subtract_button.grid(column=2, row=11, sticky=tk.W, padx=5, pady=0)

#Final Tag ID
finaltag_label = ttk.Label(root, text="Final_Tag",font=('Times', 15),background='white', foreground='red')
finaltag_label.grid(column=0, row=12, sticky=tk.W, padx=5, pady=5,ipadx=10, ipady=0)

finaltag_entry = tk.Entry(root,font=('Normal', 16),background='MediumSeaGreen', foreground='yellow')
finaltag_entry.grid(column=1, row=12, sticky=tk.EW, padx=5, pady=5, columnspan=3,ipadx=2.5, ipady=2.5)

#clear button
clear_button = tk.Button(root, text="reset",font=('Times', 12),command=clear, background='white',foreground='blue')
clear_button.grid(column=2, row=13, sticky=tk.W, padx=5, pady=0)
root.mainloop()

#sample_value = 3039606303C86A4056BB34CF