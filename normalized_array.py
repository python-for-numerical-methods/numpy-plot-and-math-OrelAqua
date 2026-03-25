import numpy as np
def normalized_array(arr):
    # מציאת ערכי המינימום והמקסימום במערך
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    
    # טיפול במקרה קצה: אם המקסימום והמינימום שווים, כל הערכים זהים
    if arr_min == arr_max:
        return np.zeros_like(arr, dtype=float)
    
    # חישוב הנרמול באמצעות פעולות וקטוריות בלבד (יוצר מערך חדש)
    normalized_arr = (arr - arr_min) / (arr_max - arr_min)
    
    return normalized_arr

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
