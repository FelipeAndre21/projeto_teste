def conj_parts(conj):
    if len(conj) == 5:
        list = []

        list.append([])

        for i in range(len(conj)):
            list.append([conj[i]])

        for i in range(len(conj)):
            for j in range(len(conj)):
                if j > i:
                    new_list = [conj[i], conj[j]]
                    list.append(new_list)

        for i in range(len(conj)):
            for j in range(len(conj)):
                for k in range(len(conj)):
                    if j > i and k > j:
                        new_list2 = [conj[i], conj[j], conj[k]]
                        list.append(new_list2)

        for i in range(len(conj)):
            for j in range(len(conj)):
                for k in range(len(conj)):
                    for y in range(len(conj)):
                        if j > i and k > j and y > k:
                            new_list3 = [conj[i], conj[j], conj[k], conj[y]]
                            list.append(new_list3)


    elif len(conj) == 4:
        list = []

        list.append([])

        for i in range(len(conj)):
            list.append([conj[i]])

        for i in range(len(conj)):
            for j in range(len(conj)):
                if j > i:
                    new_list = [conj[i], conj[j]]
                    list.append(new_list)

        for i in range(len(conj)):
            for j in range(len(conj)):
                for k in range(len(conj)):
                    if j > i and k > j:
                        new_list2 = [conj[i], conj[j], conj[k]]
                        list.append(new_list2)



    elif len(conj) == 3:
        list = []

        list.append([])

        for i in range(len(conj)):
            list.append([conj[i]])

        for i in range(len(conj)):
            for j in range(len(conj)):
                if j > i:
                    new_list = [conj[i], conj[j]]
                    list.append(new_list)





    new_list4 = conj
    list.append(new_list4)

    return list


if __name__ == '__main__':
    list = ['casa', 'sino', 'bola']
    print(conj_parts(list))
