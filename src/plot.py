import seaborn as sns
import matplotlib.pyplot as plt

def show(x, y, n):
    sns.set(style='darkgrid')
    ax = plt.subplot()
    ax.set(title='heat transfer MES', xlabel='n = ' + str(n))
    ax.plot(x, y, color='#0b216b')

    plt.show()
