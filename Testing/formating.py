# import random
#
# for i in range(10):
#     x = random.randrange(100000)
#     print(f"My number: {x:6,}")
#
# x = 5
# y = 66
# z = 777
# print(f"A - '{x}' B - '{y}' C - '{z}'")
#
# my_fruit = ["Apples","Oranges","Grapes","Pears"]
# my_calories = [4, 300, 70, 30]
#
# for i in range(4):
    # print(my_fruit[i], "are", my_calories[i], "calories.")
    # print(f"{my_fruit[i]} are {my_calories[i]} calories.")
    # print(f"{my_fruit[i]:7} are {my_calories[i]:3} calories.")

# for hours in range(1,13):
#     for minutes in range(0,60):
# #         print(f"Time {hours:02}:{minutes:02}")
# x = 0.1
# y = 123.456789
#
# print(f"{x:.1}  {y:.1}")
# print(f"{x:.2}  {y:.2}")
# print(f"{x:.3}  {y:.3}")
# print(f"{x:.4}  {y:.4}")
# print(f"{x:.5}  {y:.5}")
# print(f"{x:.6}  {y:.6}")
#
# print()
# print(f"{x:.1f}  {y:.1f}")
# print(f"{x:.2f}  {y:.2f}")
# print(f"{x:.3f}  {y:.3f}")
# print(f"{x:.4f}  {y:.4f}")
# print(f"{x:.5f}  {y:.5f}")
# print(f"{x:.6f}  {y:.6f}")
cost1 = 3.07
tax1 = round(cost1 * 0.06, 2)
total1 = cost1 + tax1

print(f"Cost:  ${cost1:5.2f}")
print(f"Tax:    {tax1:5.2f}")
print(f"-------------")
print(f"Total: ${total1:5.2f}")

cost2 = 5.07
tax2 = round(cost2 * 0.06, 2)
total2 = cost2 + tax2

print()
print(f"Cost:  ${cost2:5.2f}")
print(f"Tax:    {tax2:5.2f}")
print(f"-------------")
print(f"Total: ${total2:5.2f}")

print()
grand_total = total1 + total2
print(f"Grand total: ${grand_total:5.2f}")