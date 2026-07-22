# 1. 定義 BMI 計算函式（打造機器）
def calc_bmi(weight_kg, height_m):
    return weight_kg / height_m ** 2

# 2. 呼叫函式並印出結果（使用機器）
my_bmi = calc_bmi(70, 1.75)
print("我的 BMI 是：", my_bmi)      