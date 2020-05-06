# import some_function_name from some_file_name
# some_function_name.__code__ - Это объект который оборачивает данную функцию
# some_function_name.__code__.co_code - Это сам байт код
# import dis - disassembler
# dis.dis(some_function_name)
# import opcode
# print(opcode.opman)
