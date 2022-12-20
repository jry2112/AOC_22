day = "day10"

open(f"input/{day}_test", "x")
open(f"input/{day}_input", "x")
open(f"{day}", "x")
with open(f"{day}.py", "x") as file:
    file.write('if __name__ == "__main__":\n')
    file.write('    pass')
