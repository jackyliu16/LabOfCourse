def insert_into_all(item, nested_list):
    return [lst.insert(0, item) for lst in nested_list]

if __name__ == "__main__":
    a = [[], [1,2], [3]]
    insert_into_all(0, a)
    print(a)
    print(insert_into_all(0, a))

