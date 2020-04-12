
first_station = 1
second_station = 1
third_station = 8
fourth_station = 4

if first_station > second_station and first_station > third_station and first_station > fourth_station:
  print(1)

if second_station > first_station and second_station > third_station and second_station > fourth_station:
  print(2)

if third_station > first_station and third_station > second_station and third_station > fourth_station:
  print(3)

if fourth_station > first_station and fourth_station > second_station and fourth_station > third_station:
  print(4)

if first_station == second_station:
  print(1)

if first_station == third_station:
  print(1)

if first_station == fourth_station:
  print(1)

if second_station == third_station:
  print(2)

if second_station == fourth_station:
  print(2)

if third_station == fourth_station:
  print(3)
