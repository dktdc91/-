# range.py
# by Kevin dela Cruz for Persol Group

message_1 = "Printing current and previous numbers"
message_current = "Current Number "
message_previous = " Previous Number "
message_sum = " Sum: "

print(message_1)
for i in range(10):
    prev_int = i-1 if ((i-1) > 0) else 0
    print(message_current + str(i) + message_previous + str(prev_int) + message_sum + str (i+prev_int))
