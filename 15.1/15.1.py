#Кондратюк Егор 3ИСд-1.22
#Практическая 15 вариант 15
#Прочитать из файла двухмерный массив чисел размером
#л х ш, транспонировать его и записать полученную матрицу в новый файл. (В первой строке файлов записывается размер массива.)


def transpose_matrix(input_file, output_file):
    # Считываем исходную матрицу
    with open(input_file, 'r', encoding='utf-8') as f_in:
        n, m = map(int, f_in.readline().split())
        matrix = [list(map(int, f_in.readline().split())) for _ in range(n)]
    
    # Транспонируем матрицу
    transposed = list(zip(*matrix))
    
    # Записываем результат в новый файл
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(f"{m} {n}\n")  # Размер транспонированной матрицы
        for row in transposed:
            f_out.write(' '.join(map(str, row)) + '\n')


transpose_matrix('input.txt', 'output.txt')
