import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

init_price = 120000
years = 5
rate = 0.05
months = 5 * 12
monthly_rate = rate / 12

rate_deposit = 0.12
monthly_rate_deposit = rate_deposit / 12


def get_future_value_of_flat(rate, nper, pv):
    return npf.fv(rate, nper, 0, -pv)

def get_monthly_payment(rate, nper, fv):
    return npf.pmt(rate, nper, 0, fv)

def show_chart(months, monthly_rate,monthly_rate_deposit,pv,pm):
    time = np.arange(0, months + 1)
    prices = [npf.fv(monthly_rate, m, 0, -pv) for m in time]
    savings = npf.fv(monthly_rate_deposit, time, pm, 0)
    plt.plot(time, prices, label='Cena mieszkania', color='blue')
    plt.plot(time, savings, label='Wzrost oszczędności', color='red')
    plt.legend()
    plt.xlabel('Miesiące')
    plt.ylabel('Kwota (zł)')
    plt.show()

if __name__ == "__main__":
    fv = get_future_value_of_flat(rate, years, init_price)
    pm = get_monthly_payment(monthly_rate_deposit, months, fv)
    print(f"Przyszła wartość mieszkania po {years} latach: {fv:.2f} zł")
    print(f"Miesięczna wpłata na lokate, aby uzbierać {fv:.2f} zł: {-pm:.2f} zł")
    show_chart(months, monthly_rate, monthly_rate_deposit, init_price, pm)
