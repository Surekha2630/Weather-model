#N.SUREKHA
#VU21CSEN0100369
import matplotlib.pyplot as plt
def quadratic_temperature_model(day, a, b, c):
      temperature = a * day**2 + b * day + c
      return temperature
def main():
      a =6
      b = -3
      c = 6
      num_days = int(input("Enter the number of days to model: "))
      days = list(range(1, num_days + 1))
      temperatures = [quadratic_temperature_model(day, a, b, c) for day in days]
      plt.plot(days, temperatures,marker='o', label=f'Temperature: {a}x^2 + {b}x + {c}')
      plt.title('Weather Modeling')
      plt.xlabel('Day')
      plt.ylabel('Temperature (°C)')
      plt.legend()
      plt.show()
      
main()
