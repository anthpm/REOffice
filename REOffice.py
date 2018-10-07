listings= dict()
listings[100]=['Smith','500000','4','2','11040']
listings[105]=['Smith','125000','4','1','11240']
listings[110]=['Smith','545000','3','2','11043']
listings[115]=['Newland','545052','3','2','11043']
listings[120]=['Newland','1250000','5','3','11043']

def generateID(): #Automatically Generating a New ID for a New Home Listing

    d=max(listings)
    newid=d+5
    return newid

def newlisting(): #Creating a New Listing
    newkey=generateID();
    print('You will need to enter the following information: Agent Last Name, Price of House, Number of Bedrooms, Number of Bathrooms, Zip code\n')
    agent=input('Last name of the Agent:\n')
    price=input('House Price:\n')
    bed=input('Number of bedrooms:\n')
    bath=input('Number of bathrooms:\n')
    zipcode=input('Zip Code:\n')
    print('You have succesfully listed this house. Your new listing ID is:', newkey)
    listings[newkey]=[agent, price, bed, bath, zipcode]
    return listings[newkey]
    

def printall():   #Print All Listings 
    c=list(listings.items())
    for k,v in c:
        a,b=(v,k)
        agent=v[0]
        zipcode=v[4]
        bedrooms=v[2]
        bathrooms=v[3]
        price=v[1]
        print ('Listing Number: ',b,'|','Agent Name: ',agent,'|','Price: ',price, '| Bedrooms: ', bedrooms, '| Bathrooms :', bathrooms, '| Zip Code: ', zipcode)
    

def byagent():    #Listings By Agent Name
    name=input('Name of the Agent: ')
    c=list(listings.items())
    for k,v in c:
        a,b=(v,k)
        agent=v[0]
        price=v[1]
        byagentname={agent:[k,price]}
        listbyname=list(byagentname.items())
        
        for keys,values in listbyname:
            if name==agent:
                print ('Listing Details: ID, Price: ', values)
    if name!=agent:
        print("There are no matches")

def byzipcode():    #Listings By Zip Code
    zipcode=input('Enter Zip Code: ')
    c=list(listings.items())
    for k,v in c:
        a,b=(v,k)
        agent=v[0]
        zipc=v[4]
        bedrooms=v[2]
        bathrooms=v[3]
        price=v[1]
        byzip={zipc:[k,price,bedrooms,bathrooms,agent]}
        listbyzip=list(byzip.items())
        
        for keys,values in listbyzip:
            if zipcode==zipc:
                print ('Listing Details: ID, Price, Bedrooms, Bathrooms, Name of Agent:', values)
    if zipcode!=zipc:
        print("There are no matches")

def bybedroom():    #Listings By Number of Bedrooms
    num=input('Enter Number of Bedrooms: ')
    c=list(listings.items())
    for k,v in c:
        a,b=(v,k)
        agent=v[0]
        price=v[1]
        bedroom=v[2]
        bathrooms=v[3]
        zipcode=v[4]      
        bybed={bedroom:[k,price,bathrooms,zipcode,agent]}
        listbybed=list(bybed.items())
        for keys,values in listbybed:
            if num == bedroom:
                print ('Listing Details: ID, Price, Bathrooms, Zipcode, Name of Agent:', values)
    if num!=bedroom:
        print("There are no matches")

def bybathroom():    #Listings By Number of Bathrooms
    num=input('Enter Number of Bathrooms: ')
    c=list(listings.items())
    for k,v in c:
        a,b=(v,k)
        agent=v[0]
        price=v[1]
        bedroom=v[2]
        bathrooms=v[3]
        zipcode=v[4]      
        bybath={bathrooms:[k,price,bedroom,zipcode,agent]}
        listbybath=list(bybath.items())
        for keys,values in listbybath:
            if num == bathrooms:
                print ('Listing Details: ID, Price, Bedrooms, Zipcode, Name of Agent:', values)
    if num!=bathrooms:
        print("There are no matches")

def byprice():    #Listings By Price Range
    print('Select a price range:\n', '(1) Less than $250,000\n','(2) $250,0001-$500,000\n', '(3) $500,001-$700,000\n', '(4) More than $700,000\n')
    num=int(input('Option '))
    c=list(listings.items())
    for k,v in c:
        a,b=(v,k)
        agent=v[0]
        price=v[1]
        newprice=int(price)
        bedroom=v[2]
        bathrooms=v[3]
        zipcode=v[4]      
        byprice={newprice:[b,bedroom,bathrooms,zipcode,agent]}
        listbyprice=list(byprice.items())
        for key in listbyprice:
            if newprice in range (0, 250000):
                print('Price Match: ','$', newprice)
                print(('Listing Details: ', byprice[newprice]))                     
            elif newprice in range (250001, 500000):
                print('Price Match: $', newprice)
                print(('Listing Details: ',byprice[newprice]))
            elif newprice in range (500001, 700000):
                print('Price Match: ','$', newprice)
                print(('Listing Details: ',byprice[newprice]))
            elif newprice in range(700001, 10000000):
                print('Price Match: ','$', newprice)
                print(('Listing Details: ',byprice[newprice]))
            


def searchHome():
    print('How would you like to search for a house?\n', '(1) By Zip Code\n', '(2) By Number of Bedrooms\n', '(3) By Number of Bathrooms\n', '(4) By Price\n')
    answer=input('Option: ')
    while answer=='1':
        byzipcode()
        break
    while answer=='2':
        bybedroom()
        break
    while answer=='3':
        bybathroom()
        break
    while answer=='4':
        byprice()
        break

           
    
def main():
    
    print('Please select what you would like to do:\n', '(1) Enter a new listing\n', '(2) Search for a House\n', '(3) Print all listings\n', '(4) Print listings by Agent\n')
    answer=input('Option: ')
    while answer== '1':
        newlisting()
        break    
    while answer== '2':
        searchHome()
        break
    while answer== '3':
        printall()
        break
    while answer=='4':
        byagent()
        break    
main()



 #values=list(listbyagent.items())
        #sortedlist=values.sort()
        #for i in values:
            
        
        #print ('Last Name of agent:', agent,'|','Listing Number:',b)
        #print (sortedlist)
        

 #answer=input("Do you want to enter a new Home--Yes or No): ")
    #while answer=='Yes' or 'yes':
    #    newlisting()
    #   print('\n')
    #   break
    #while answer== 'No' or 'no':
    #   print("Thank you you are now exiting the program")
    #   break



#def updatelist():
    
   # listings.update() 


#for i in listbyprice:
            #newprice=listbyprice[0]
            #print (newprice)
