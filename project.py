import gurobi
from gurobipy import *
import math
import csv
import pandas as pd
import numpy as np

m = Model("ModelA")

#data
warehouse_regions = pd.read_csv('WarehouseRegions.csv', header = 0)
warehouses = list(range(1, len(warehouse_regions['Warehouse ID'])+1)) #list of warehouses
product_weight = pd.read_csv('ProductWeight.csv', header = 0)
products = list(range(1,len(product_weight['Product ID'])+1)) #list of products 
order_regions = pd.read_csv('OrderRegions.csv', header = 0)
orders = list(range(1,len(order_regions['Order ID'])+1)) 

inventory_df = pd.read_csv('Warehouses.csv', header = 0)
stock = inventory_df['Stock'].to_numpy()
I = {} #this variable will be the number of inventory at warehouse i of product k
i = 0
for warehouse in warehouses:
    for product in products:
        I[warehouse,product] = stock[i]
        i = i+1
        
# =============================================================================
# deliverycost_df = pd.read_csv('DeliveryCost.csv', header = 0)
# C = {} #delivery cost of order j from warehouse i 
# indexx = list(range(0,len(warehouse_regions['Warehouse ID'])))
# cost = []
# 
# # =============================================================================
# #     cost.append(deliverycost_df[str(m)].to_numpy())
# # =============================================================================
# for i in indexx:
#     cost.append(deliverycost_df.loc[i]).to_numpy()
# # =============================================================================
# #     for m in orders:
# #         deliverycost_df[str(m)].to_numpy()
# # =============================================================================
#         
# for warehouse in warehouses:
#     for order in orders:
#         C[warehouse, order] = deliverycost_df.loc
# =============================================================================
 


D = {} # demand of product k in order j



weight = product_weight['Weight'].to_numpy()
W = {} #weight of product k
k = 0
for product in products:
    W[product] = weight[k]
    k = k+1
    


    
    

            
        

#Data



#Variables
#x = m.addVars(range(1, N+1), range(1, M+1), range(1, k+1), ub = 1, name = 'x' )