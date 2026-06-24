import pandas as pd
data={
"Item":["Pizza","Burger","Fried rice","Parotta","Parotta","Pizza","Juice","Parotta","Briyani","Pizza","Fried rice","Briyani","Fried rice"],
"Location":["Chennai","Madurai","Trichy","Madurai","Karaikudi","Chennai","Coimbatore","Chennai","Madurai","Trichy","Karaikudi","Karaikudi","Coimbatore"],
"Time":["1 pm","2 pm","5 pm","7 pm","9 am","10 am","12 pm","7 pm","1 pm","4 pm","5 pm","1 pm","5 pm"]
}
df=pd.DataFrame(data)
Time_analyze=df.Time
print("Time_analyze\n",Time_analyze)
Item_order=df.Item
print("Item\n",Item_order)
Ordered_location=df.Location
print("Location\n",Ordered_location)