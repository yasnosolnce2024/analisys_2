import pandas as pd

data = {
    "Имя": ["Анна", "Борис", "Виктор", "Галина", "Дмитрий", "Елена", "Жанна", "Захар", "Ирина", "Кирилл"],
    "Математика": [85, 90, 78, 92, 88, 76, 95, 89, 84, 91],
    "Физика": [80, 85, 79, 94, 87, 77, 90, 86, 83, 88],
    "Химия": [78, 88, 84, 90, 85, 79, 92, 87, 80, 86],
    "Биология": [82, 86, 77, 91, 89, 75, 88, 85, 81, 90],
    "Информатика": [88, 92, 80, 94, 90, 78, 96, 89, 85, 93]
}

df = pd.DataFrame(data)

print("Первые несколько строк DataFrame:")
print(df.head())

mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"\nQ1 для Математики: {Q1_math}")
print(f"Q3 для Математики: {Q3_math}")
print(f"IQR для Математики: {IQR_math}")

std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev)