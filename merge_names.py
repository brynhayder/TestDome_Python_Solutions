def unique_names(names1, names2):
    x = set(names1)
    y = set(names2)
    return list(x.union(y))

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
