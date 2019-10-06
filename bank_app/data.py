import psycopg2
import csv
import pandas as pd
con=psycopg2.connect(host="ec2-23-21-177-102.compute-1.amazonaws.com",
                    database="d4ss49mldhtf0u",
                    user="soildyclqdtopj",
                    password="2c8b1348e6ebc0fe9bd88aeb2298ca23d6d8183828e31f8064e4261dd886cc90",
                    port='5432',
        )
cur=con.cursor()
#csv_data = csv.reader(file('.csv'))
print("going")
x=pd.read_csv("bank_branches.csv")
l=len(x)
#y=(1,"lko","maholi",)
query =  "INSERT INTO app_banks_branches (ifsc,bank_id,branch,address,city,district,state,bank_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
for i in range(l):
     y=(x["ifsc"][i],str(x["bank_id"][i]),x["branch"][i],x["address"][i],x["city"][i],x["district"][i],x["state"][i],x["bank_name"][i],)   
     cur.execute(query,y)
con.commit()

print ("Done")

cur.close()

con.close()
