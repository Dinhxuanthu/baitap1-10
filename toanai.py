import matplotlib.pyplot as plt

# Hàm mục tiêu f(x)
def f(x):
    return x**2 + 6*x + 8

# Đạo hàm của hàm mục tiêu f'(x)
def f_prime(x):
    return 2*x + 6

# Thuật toán Gradient Descent
def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    f_values = []  # Lưu giá trị của f(x) tại mỗi bước lặp

    for i in range(num_iterations):
        f_values.append(f(x))
        
        # Cập nhật giá trị x theo Gradient Descent
        gradient = f_prime(x)
        x = x - learning_rate * gradient

    return f_values

# Hàm để chạy thuật toán với nhiều learning rate khác nhau và vẽ đồ thị
def run_experiment(learning_rates, starting_point, num_iterations):
    plt.figure(figsize=(10, 6))

    for lr in learning_rates:
        f_values = gradient_descent(starting_point, lr, num_iterations)
        plt.plot(range(num_iterations), f_values, label=f'learning rate = {lr}')

    plt.title('Impact of Learning Rate on Convergence')
    plt.xlabel('Iterations')
    plt.ylabel('f(x) values')
    plt.legend()
    plt.grid(True)
    plt.show()

# Các giá trị learning rate cần thử nghiệm
learning_rates = [0.001, 0.01, 0.1, 1.0]
starting_point = 0
num_iterations = 50

# Chạy thí nghiệm với các learning rate khác nhau
run_experiment(learning_rates, starting_point, num_iterations)
