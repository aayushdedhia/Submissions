def count_walk_aways(n, s):
    computers = 0
    in_cafe = set()
    walk_aways = 0
    walk_away = set()

    for customer in s:
        if customer in in_cafe:
            in_cafe.remove(customer)
            computers -= 1
        else:
            if computers < n:
                computers += 1
                in_cafe.add(customer)
            else:
                if customer in walk_away:
                    pass
                else:
                    walk_away.add(customer)
                    walk_aways += 1

    return walk_aways



n = int(input("Enter number: "))
s = input("Enter String: ")
print(count_walk_aways(n, s))
