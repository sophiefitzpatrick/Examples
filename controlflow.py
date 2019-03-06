# CodeAcademy: Python Control Flow Project: Finding the cheapest shipping by weight

def ground_shipping(weight):
  cost = 20 + (4.75 * weight)
  if weight <= 2:
    cost = 20 + (1.5 * weight)
  elif weight <= 6:
    cost = 20 + (3 * weight)
  elif weight <= 10:
    cost = 20 + (4 * weight)
  return cost

print(ground_shipping(8.4))

premium_ground = 125

def drone_shipping(weight):
  cost = 14.25 * weight
  if weight <= 2:
    cost = 4.5 * weight
  elif weight <= 6:
    cost = 9 * weight
  elif weight <= 10:
    cost = 12 * weight
  return cost
 
print(drone_shipping(1.5))

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  premium = premium_ground
  drone = drone_shipping(weight)
  if ground < drone and ground < premium:
    method = "ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium"
    cost = premium
  else:
    method = "drone"
    cost = drone
  print("The cheapest price available is 	$%.2f with %s method" % (cost, method))
  
cheapest_shipping(41.5)