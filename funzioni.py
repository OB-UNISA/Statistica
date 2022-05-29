import pandas as pd
from IPython.display import display
from matplotlib import pyplot as plt


def modalita_del_carattere(elements):
    # fa diventare gli elementi un insieme per eliminare i duplicati e poi ordina
    return sorted(set(elements))


def frequenza_assoluta(elements):
    freq = []
    ordered_elements = sorted(elements)
    freq.append(1)

    for i in range(1, len(ordered_elements)):
        if ordered_elements[i] == ordered_elements[i - 1]:
            # incrementa il valore della frequenza dell'ultima frequenza
            freq[-1] += 1
        else:
            # aggiunge una nuova frequenza
            freq.append(1)

    return freq


def frequenza_cumulativa_assoluta(freq_assoluta):
    cum_freq = [freq_assoluta[0]]
    for i in range(1, len(freq_assoluta)):
        # aggiunge la frequenza cumulativa usando la relazione di ricorrenza
        cum_freq.append(cum_freq[i - 1] + freq_assoluta[i])

    return cum_freq


def frequeza_relativa(n, freq_assoluta):
    freq_relativa = []
    for i in range(len(freq_assoluta)):
        freq_relativa.append(freq_assoluta[i] / n)

    return freq_relativa


def frequenza_cumulativa_relativa(n, freq_comulativa_assoluta):
    freq_cumulativa_relativa = []
    for i in range(len(freq_comulativa_assoluta)):
        freq_cumulativa_relativa.append(freq_comulativa_assoluta[i] / n)

    return freq_cumulativa_relativa


def print_stat(name, stats):
    len_stats = len(stats)
    for i in range(len_stats - 1):
        print(f'{name}_{i + 1} = {stats[i]}', end=', ')
    print(f'{name}_{len_stats - 1} = {stats[len_stats - 1]}')


def summary_table(modalita, freq_assoluta, freq_relativa, freq_cumulativa_assoluta, freq_cumulativa_relativa):
    data_table = []
    for i in range(len(modalita)):
        data_table.append([i + 1, modalita[i], freq_assoluta[i], freq_relativa[i], freq_cumulativa_assoluta[i],
                           freq_cumulativa_relativa[i]])

    df = pd.DataFrame(data_table, columns=['i', 'v_i', 'f_i', 'p_i', 'F_i', 'P_i'])
    df.set_index('i', inplace=True)
    display(df)


def grafico_a_linee(xs, ys, title=None, xlabel=None, ylabel=None, grid=False):
    fig, ax = plt.subplots()
    ax.plot(xs, ys, '-o')
    add_labels_on_points(xs, ys)
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if grid:
        ax.grid()

    plt.show()


def add_labels_on_points(xs, ys):
    for x, y in zip(xs, ys):
        label = "{:.2f}".format(y)

        plt.annotate(label,
                     (x, y),
                     textcoords="offset points",
                     xytext=(0, 7),
                     ha='center')


def grafico_a_torta(labels, values, title=None):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    if title:
        ax.set_title(title)

    plt.show()


def classi_valori_contigui(elements, ampiezza=5, grid=False, title=None, xlabel=None, ylabel=None, plot=False):
    min_value = min(elements)
    max_value = max(elements)

    fig, ax = plt.subplots()
    values, bins, bars = ax.hist(elements, bins=list(range(min_value, max_value + ampiezza, ampiezza)),
                                 edgecolor='black', linewidth=1.5)

    if plot:
        ax.set_xticks(bins)
        ax.bar_label(bars)
        if grid:
            ax.grid()
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)

        plt.show()

    classi = {}
    for i in range(len(bins) - 1):
        classi[bins[i]] = values[i]

    return classi
