# root directory tests.py

from functions.get_files_info import get_files_info

print("Result for current directory:")
current_result = get_files_info("calculator", ".")
# print(current_result)

print("Result for 'pkg' directory:")
pkg_result = get_files_info("calculator", "pkg")
# print(pkg_result)

print("Result for '/bin' directory:")
bin_result = get_files_info("calculator", "/bin")
print(bin_result)

print("Result for '../' directory")
root_result = get_files_info("calculator", "../")
print(root_result)


        



