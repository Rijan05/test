marks = [45, 67, 32, 89, 90, 29]
pass_count = 0
fail_count = 0
for m  in marks:
 if m >= 40:
    pass_count+=1
 else:
    fail_count+=1
print("passed:",pass_count)
print("failed:", fail_count)