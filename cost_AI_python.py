def ground_shipping(weight):
  flat_charge = 20.00
  if weight <= 2:
    price_per_pound = 1.50 * weight
  elif weight > 2 and weight <= 6:
    price_per_pound = 3.00 * weight
  elif weight > 6 and weight <= 10:
    price_per_pound = 4.00 * weight
  else:
    price_per_pound = 4.75 * weight
  cost = price_per_pound + flat_charge
  return(cost)

premium_ground_shipping = 125.00

def drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50 * weight
  elif weight > 2 and weight <= 6:
    price_per_pound = 9.00 * weight
  elif weight > 6 and weight <= 10:
    price_per_pound = 12.00 * weight
  else:
    price_per_pound = 14.25 * weight
  cost = price_per_pound
  return(cost)

def cost_AI(weight):
  ground_shipping_price = ground_shipping(weight)
  drone_shipping_price = drone_shipping(weight)
  if ground_shipping_price < drone_shipping_price and ground_shipping_price < premium_ground_shipping:
    return(f"For a package of {weight} lbs, our system detected that ground shipping will the cheapest, ${ground_shipping_price}. Premium is ${premium_ground_shipping} and drone is ${drone_shipping_price}")
  elif drone_shipping_price < ground_shipping_price and drone_shipping_price < premium_ground_shipping:
    return(f"For a package of {weight} lbs, our system detected that drone shipping will the cheapest, ${drone_shipping_price}. Premium is ${premium_ground_shipping} and ground is ${ground_shipping_price}")
  elif premium_ground_shipping < ground_shipping_price and premium_ground_shipping < drone_shipping_price:
    return(f"So finally {premium_ground_shipping} pre-ground is better now. as drone costs {drone_shipping_price} and ground costs {ground_shipping_price}")


user_weight = float(input("Welcome! How many lbs of package do you have?: "))

print(cost_AI(user_weight))

input()