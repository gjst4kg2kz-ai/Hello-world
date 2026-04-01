#Prevents bad input (like negative numbers)
edge_length = int(input("Enter the length of a cube's edge: "))

if edge_length <= 0:
    print("Edge length must be positive.")
else:
    surface_area = 6 * edge_length ** 2
    print("The surface area of the cube is:", surface_area)
