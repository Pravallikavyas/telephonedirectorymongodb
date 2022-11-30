#Importing the pymongo package to connect python and mongodb
import pymongo
#Creating a variable client to assign mongoclient instance
client = pymongo.MongoClient()
#Creating a database telephonedirectory
db = client["telephonedirectory"]
#Creating a collection tel_dir
tb = db["tel_dir"]
#A function to insert data into telephone directory
def insert_details( ):
    #Creating a index in order to avoid duplicate insertion of data
    tb.create_index("Name",unique=True)
    #Creating a document
    data1={"Name":"Pravallika.M","Mob_no":"8973636837","Place":"Chennai"}
    #A query to insert single document
    x=tb.insert_one(data1)
    #Creating a list mydata to store many documents
    mydata=[{"Name":"Sai Sri Harsha.M","Mob_no":"9445703019","Place":"Chennai"},
        {"Name":"Venkata Naresh.K","Mob_no":"9884996909","Place":"Trichy"},
        {"Name":"Soumiya.S","Mob_no":"9444444502","Place":"Chennai"},
        {"Name":"Saranya.S","Mob_no":"9790026468","Place":"Chennai"},
        {"Name":"Sirisha.L","Mob_no":"8778762443","Place":"Kadapa"},
        {"Name":"Sravani.V","Mob_no":"7010807109","Place":"Ujjain"},
        {"Name":"Sridevi.K","Mob_no":"7871133554","Place":"Chennai"},
        {"Name":"Venkata Ramana.K","Mob_no":"9444188519","Place":"Chennai"},
        {"Name":"Divya Sree.V","Mob_no":"9493472065","Place":"Kadapa"},
        {"Name":"Padmaja.M","Mob_no":"9710331942","Place":"Chennai"},
        {"Name":"Jahnavi.K","Mob_no":"8106564198","Place":"Trichy"}]
    #A query to insert many documents into telephone directory
    y=tb.insert_many(mydata)
    #Prints insert object details.Here there will occur a duplicate key error if we try to insert duplicate data.So only unique documents will be inserted.
    print(y)
#A function to find details in telephone directory
def find_details( ):
   #A query to find document in a collection whose name is "Pravallika.M"
   z=db.tb.find({"Name":"Pravallika.M"})
   #Prints find object details
   print(z)
   #A query to find document in a collection whose name is "Sai Sri Harsha.M"
   a=db.tb.find({"Name":"Sai Sri Harsha.M"},{"Place":0,"Mob_no":1})
   #Prints find object details
   print(a)
#A function to update details in telephone directory
def update_details( ):
   #A query to update details
   b=db.tb.update_one({"Name":"Saranya.S"},{"$set":{"Place":"Goa"}})
   #Print update object details
   print(b)
#A function to delete details in telephone directory
def delete_details( ):
   #A query to delete details whose name is "Soumiya.S"
   c=tb.delete_many({"Name":"Soumiya.S"})
   #Print delete object details
   print(c)
#A function to retrieve details from telephone directory
def retrieve_details( ):
   #Prints all documents present in collection
   for i in tb.find():
      print(i)
#Prompting the user to insert,find,update,delete,retrieve
while(True):
   choice=int(input("Enter your choice: "))
   match choice:
        case 1:
            a=input("Do you want to insert data?")
            if(a=="yes"):
              insert_details( )
            else:
              break

        case 2:
             b=input("Do you want to find any data?")
             if(b == "yes"):
                find_details( )
             else:
                break

        case 3:
             c= input("Do you want to update data?")
             if(c== "yes"):
                update_details( )
             else:
                 break

        case 4:
            d = input("Do you want to delete data?")
            if(d == "yes"):
               delete_details( )
            else:
                break

        case 5:
            e = input("Do you want to retrieve data?")
            if(e == "yes"):
               retrieve_details( )
            else:
                break






