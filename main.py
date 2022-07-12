#Dictionaries
# Write a program to check whether a given key exists in a dictionary or not.

# def person():
#     dict={1:'anena', 2:'beatrice', 3:'nenzy'}
#     i= int(input("enter value"))
#     for i in dict.keys():
#          print("true")
#     else:
#          print("false")    

# person()  
 

#Write a program to iterate over dictionary items using for loop.
# def colors():
#     dict={1:"blue", 2:"red", 3:"pink", 4:"yellow"}
#     for key,value in dict.items():
#         print(f"the key {key} is for {value}")
# colors()        


#Write a program to print only keys of a dictionary.
#Write a program to print values of dictionary.

# def color():
#     dict={1:"red", 2:"orange",3:"purple"}
#     # for key in dict.keys():
#     values = dict.values()
#     print(values)
# color()   

#Write a program in python to map 2 lists into a dictionary.
# def map():
#     list1=[1,2,3]
#     list2=["cat","chair","cup"]
#     dict1 =dict(zip(list1,list2))
#     x=dict1.remove[1]
#     print(dict1)
# map()    

#the del keyword removes a particular key from the dictionary
# def color():
#     dict={1:"red", 2:"orange",3:"purple"}
#     del dict[1]
#     print (dict)
# color()   

#the clear() keyword removes all items in the dictionary
# def color():
#     dict={1:"red", 2:"orange",3:"purple"}
#     dict.clear()
#     print (dict)
# color()   

# def color():
#     dict={4:"four", 5:"five", 6:"six"}
#     dict.pop(4)
#     print(dict)
# color()    

#removes the last item in the 
# def color():
#     dict={4:"four", 5:"five", 6:"six"}
#     dict.popitem()
#     print(dict)
# color()  

#print a list in ascending or descending 
# def color():
#       key_values={4:"bananas", 6:"ann",5:"apple"}
#     #   l = list(a.items())
#     #   for i in sorted(key_values.values()):
#     #     print(i,key_values[i])

#       sorted_dict=sorted(key_values)
#       print(sorted_dict)

    

#     #   l.sort(reverse="true")
# color()      
  

#sorting a list of dictionaries using the lamba method
# def mylist():
#          my_list = [{ "name" : "Will", "age" : 56},
#           { "name" : "Rob", "age" : 20 },
#           { "name" : "Mark" , "age" : 34 },
#           { "name" : "John" , "age" : 24 }]

#          print (sorted(my_list, key=lambda i: i["age"],reverse=True))
# mylist()         

def DupSearch(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i]==list[j]:
                 print "Duplicate found"
                 return
        print "No duplicated"