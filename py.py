def split_and_join(line):
    # 1. Pecah string menjadi list berdasarkan spasi
    words = line.split(" ")
    
    # 2. Gabungkan kembali list tersebut dengan tanda "-"
    result = "-".join(words)
    
    return result

if __name__ == '__main__':
    # Di Python 3, input() sudah cukup untuk mengambil string
    line = input()
    result = split_and_join(line)
    print(result)
