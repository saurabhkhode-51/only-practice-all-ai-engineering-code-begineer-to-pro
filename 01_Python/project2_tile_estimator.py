print("--- Square Room Tile & Budget Estimator---")

#input lena our float me convert karana 
room_side = float(input("enter room side length in feet: "))
tile_rate = float(input("Enter tile rate par sq. ft. (Rs.): "))

#calculations
total_area = room_side * room_side
total_cost = total_area * tile_rate

# output
print("\n--- Estimation Summary ---")
print("Total Area Of Room:", total_area,"sq. ft. ")
print("Total Budget Requered:", total_cost)