original_list = [10, 11, 12, 13, 14, 15]
new_list = [original_list[len(original_list) - i]
            for i in range(1, len(original_list)+1)]
print(new_list)