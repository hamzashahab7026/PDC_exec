import pandas as pd
import time


students_file_path = "C:/Users/Guru Group/Desktop/students.csv"
fees_file_path = "C:/Users/Guru Group/Desktop/fees.csv"


students_df = pd.read_csv(students_file_path)
fees_df = pd.read_csv(fees_file_path)


start_time = time.time()


fees_df['Day'] = fees_df['Payment Date'].str.extract(r'(\d+)$').astype(int)


payment_day_count = {}

for _, row in fees_df.iterrows():
    student_id = row['Student ID']
    payment_day = row['Day']
    if student_id not in payment_day_count:
        payment_day_count[student_id] = {}
    if payment_day not in payment_day_count[student_id]:
        payment_day_count[student_id][payment_day] = 1
    else:
        payment_day_count[student_id][payment_day] += 1

most_frequent_payment_day = {}
for student_id, day_count in payment_day_count.items():
    most_frequent_payment_day[student_id] = max(day_count, key=day_count.get)

consistent_payment_days = pd.DataFrame(list(most_frequent_payment_day.items()), columns=['Student ID', 'Most Consistent Payment Day'])

merged_df = pd.merge(students_df, consistent_payment_days, on='Student ID', how='inner')

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution Time: {execution_time:.4f} seconds")
print(merged_df.head())
