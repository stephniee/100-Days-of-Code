# Accessible anywhere
my_global_var = 1


def my_function():
    # Only accessible within my_function()
    my_local_var = 2
    print(f"local var: {my_local_var}")

my_function()
for _ in range(10):
    # Accessible anywhere
    my_block_var = 3
    print(f"global var: {my_block_var}")