def max_distance(fuel_capacity, fuel_efficiency, tire_weight):
  max_distance = 0
# store maximum distance for unit of fuel used
  dp = [0] * (fuel_capacity + 1)
  for fuel_used in range(1, fuel_capacity + 1):
    remaining_fuel = fuel_capacity - fuel_used
    distance = fuel_used * fuel_efficiency
    if remaining_fuel >= tire_weight:
      distance += (fuel_capacity - remaining_fuel - tire_weight) * fuel_efficiency
# Update maximum distance used
    dp[fuel_used] = max(dp[fuel_used - 1], distance)
  return dp[fuel_capacity]
# example usage
fuel_capacity = 10 # max fuel capacity
fuel_efficiency = 20 # miles per gallon
tire_weight = 2 # weight of spare tire
max_dist = max_distance(fuel_capacity, fuel_efficiency, tire_weight)
print("Maximum distance the spare tire can travel:", max_dist, "miles")
