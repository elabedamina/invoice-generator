Company_Slogan = 'Parfums et Cie SARL'
Street_Address = '1 route des Joliettes'
City_ZIP = '84250 Grans'
phone = '06 60 68 88 97'
fix= '04 65 89 78 78'
Date= "01/03/2024"
Expiration_Date= "01/05/2024"
num_invoice= 'CC-0021'

#Customer#
Name_Customer= 'Dubard cosmétiques SAS'
Company_Name_Customer= 'Les soins d Antan'
Address_Customer= '1 côte du Touron'
City_ZIP_Customer= '01120 La Perche Ferté'
Phone_Customer= '05 45 45 45 45'
#Ship to#
Name_Ship= 'Dubard cosmétiques SAS'
Company_Name_Ship= 'Les soins d Antan'
Address_Ship= '1 côte du Touron'
City_ZIP_Ship= '01120 La Perche Ferté'
Phone_Ship= '05 45 45 45 45'
#Shipping details#
Air_Ocean= 'Air'
Est_Ship_Date= '12/04/2024'
weight_units_Groos= 'KG'
weight_units_Cubic= ''
Total_Package= '14'
#products#
product1_id= '1'
product1_unit= 'ml'
product1_name= 'Flacons 100 ml - type cirus'
product1_qty= 5000
product1_up= 0.9
product1_total= product1_qty * product1_up

product2_id= '2'
product2_unit= 'ml'
product2_name= 'Flacons 50 ml - type zéphir'
product2_qty= 10000
product2_up= 0.5
product2_total= product2_qty*product2_up

#billing#
subtotal= product2_total + product1_total
taxabale= subtotal
tax_rate= 20
tax= subtotal * (tax_rate/100)
freight=0
inssurance=0
legal_consular=0
inspection=0
other=0
total_price= taxabale + tax + freight +inssurance +legal_consular+inspection+other

#Additional details#
country_origins= 'France'
Port_Embarkation= 'Marseillia'
Port_Discharge= 'Skikda'

condition_payement = "Letter of Credit"
other_information = ""
#########################################


context = {"Company_Slogan" : Company_Slogan, "Street_Address" : Street_Address,"City_ZIP" : City_ZIP,
            "phone" :phone,"fix": fix,"Date": Date,"Expiration_Date":Expiration_Date,
            "num_invoice": num_invoice, "Name_Customer": Name_Customer,
            "Company_Name_Customer":Company_Name_Customer,"Address_Customer": Address_Customer,
            "City_ZIP_Customer": City_ZIP_Customer,"Phone_Customer": Phone_Customer,
            "Name_Ship": Name_Ship,"Company_Name_Ship": Company_Name_Ship,
            "Address_Ship": Address_Ship,"City_ZIP_Ship": City_ZIP_Ship,
            "Phone_Ship":Phone_Ship,"Air_Ocean":Air_Ocean,"Est_Ship_Date": Est_Ship_Date,
            "weight_units_Groos": weight_units_Groos,"weight_units_Cubic": weight_units_Cubic,"Total_Package": Total_Package,
            "product1_id": product1_id, "product1_unit": product1_unit,
            "product1_unit": product1_unit, "product1_qty": product1_qty,
            "product1_up":product1_up,"product1_total": product1_total,
            "product2_id": product2_id,"product2_unit": product2_unit,
            "product2_name": product2_name,"product2_qty": product2_qty,
            "product2_up":product2_up,"product2_total": product2_total,
            "subtotal": subtotal,"taxabale":taxabale,
            "tax_rate":tax_rate,"tax": tax,"freight":freight,"inssurance":inssurance,
            "legal_consular":legal_consular,"inspection":inspection,
            "other":other,"total_price": total_price,"country_origins": country_origins,"Port_Embarkation": Port_Embarkation,
            "Port_Discharge": Port_Discharge,"condition_payement" :condition_payement,"other_information" :other_information,
           }