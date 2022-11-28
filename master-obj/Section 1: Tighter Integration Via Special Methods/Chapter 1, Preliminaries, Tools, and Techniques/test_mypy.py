def F(n: int) -> int:
    if n in (0, 1):
        return 1
    else:
        return F(n-1) + F(n-2)
print("Good Use", F(8))
print("Bad Use", F(355/113))


# 使用mypy检查
# mypy master-obj/test/test_mypy.py 
# @puzzledstorm ➜ /workspaces/python-programs (main ✗) $ mypy  master-obj/test/test_mypy.py 
# master-obj/test/test_mypy.py:7: error: Argument 1 to "F" has incompatible type "float"; expected "int"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)