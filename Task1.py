# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988
import decimal

num = decimal.Decimal(897.1435431541345)
print(f'Дано число - {num}')
size = (input('Задайте точность числа (пример - 0.00) - '))
print(num.quantize(decimal.Decimal(f'{size}')))








# #exit()

# n = decimal.Decimal(2.12) + decimal.Decimal(1.345)
# print(n)
# a = 1.1346
# b = 2.213412
# decimal.getcontext().prec = 3
# print(decimal.Decimal(2.12) + decimal.Decimal(1.345))
# with decimal.localcontext() as txt:
#     txt.prec = 3
#     print(decimal.Decimal(2.12) + decimal.Decimal(1.345))
# print(decimal.Decimal(n))

# n = decimal.Decimal(2.12 * 1.34)
# print(n)
# print(n.quantize(decimal.Decimal('0.000')))
# print(round(2.67564, 2))
# b = decimal.Decimal(2.67564)
# print(b.quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_UP ))
