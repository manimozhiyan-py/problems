# Replace eeach element by Rank

arr = [20, 15, 25, 30, 15]

class Rank:
    def increase(self, arr):
        sorted_arr = arr[:]
        for i in range(len(sorted_arr)-1):
            for j in range(i+1, len(sorted_arr)):
                if sorted_arr[i] > sorted_arr[j]:
                    sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]
        return sorted_arr

    def making_dic(self, dup):
        count = 1
        dup = self.increase(dup)
        dic ={}
        for element in dup:
            if element in dic:
                pass
            else:
                dic[element] = count
                count += 1
        return dic

    def ranking(self, arr):
        output = []
        dic = self.making_dic(arr)
        for element in arr:
            output.append(dic[element])
        return output


def making_dic(arr):
    sorted_arr = sorted(set(arr))
    dic = {value: (index +1 if value < 25 else index +10) for index, value in enumerate(sorted_arr)}
    return dic

def ranking(arr):
    dic = making_dic(arr)
    output = [dic[element] for element in arr]
    return output


print(making_dic(arr))