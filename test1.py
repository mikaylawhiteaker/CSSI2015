# # mikayla
#
# '''
# a = True
# b = False
# if a and b:
#     print '1'
# elif a or b:
#     print '2'
# else:
#     print "3"
#
#
# def sales_tax(subtototal, tax_rate):
#     return subtototal * tax_rate
#
# print sales_tax(100, 0.1)
#
# def fizzBuzz(int):
#     a = int % 5 == 0
#     b = int % 3 == 0
#     if a and b:
#         return 'fizzbuzz'
#     elif a:
#         return "buzz"
#     elif b:
#         return 'fizz'
#     else:
#         return ''
#
# print fizzBuzz(18)
# '''
#
# '''
# i = 0
# while i < 10:
#     print i
#     i += 1
#
#
# for i in range(100):
#     print i + 1
# '''
# '''
# import random
#
# number_dice_roll_sum = 0.0
#
#
#
# def rollcount():
#     number_dice_roll = 0
#     global number_dice_roll_sum
#
#     double6 = False
#
#     while double6 == False:
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#
#
#         if dice1 == 6 and dice2 == 6:
#             double6 = True
#
#
#         number_dice_roll += 1
#         number_dice_roll_sum += 1
#
#
# def average():
#     print number_dice_roll_sum
#     print number_dice_roll_sum / 10000
#
#
#
# for x in range(10000):
#     rollcount()
#
# print average()
# '''
'''
d = {}
while True:
    word = raw_input('Please enter word: ')



    if word not in d:
        d[word] = 1

    else:
        d[word] += 1

    print d

    '''
