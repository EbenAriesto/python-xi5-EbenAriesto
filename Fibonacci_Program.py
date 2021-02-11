# import modul
import Fibonacci_Modul

# pemanggilan fungsi pertama
print(Fibonacci_Modul.fib1(100))

# pemanggilan fungsi kedua
print(Fibonacci_Modul.fib2(100))

# pemanggilan fungsi dengan nama lokal
fib = Fibonacci_Modul.fib1
print(fib(100))