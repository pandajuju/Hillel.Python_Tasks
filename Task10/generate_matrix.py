import matrix


n, m = int(input("Введіть розмір n: ")), int(input("Введіть розмір m: "))

mx = matrix.generate_matrix(n,m)
mx = matrix.sort_matrix(mx, n)
matrix.print_matrix(mx)