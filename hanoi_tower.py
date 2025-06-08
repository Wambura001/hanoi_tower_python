def hanoi_tower(n, source, destination, auxiliary):
  if n == 1:
    print(f"Move disk 1 from {source} to {destination}")
    return 
  hanoi_tower(n - 1, source, auxiliary, destination)
  print(f"Move disk {n} from {source} to {destination}")
  hanoi_tower(n - 1, auxiliary, destination, source)

# Example
hanoi_tower(4, "A", "B","C")
