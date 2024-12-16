import time

start_time = time.time()

def function_one():
    for i in range(5):
        print(f"Function One - iteration {i+1}")
        time.sleep(1)

def function_two():
    for i in range(5):
        print(f"Function Two - iteration {i+1}")
        time.sleep(1.5)

function_one()
function_two()

end_time = time.time()
res_time = end_time - start_time
print(res_time)