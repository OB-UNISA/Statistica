import pandas as pd


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


def frequenzaa_comulativa_assoluta(freq_assoluta):
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


def print_data_table(modalita, freq_assoluta, freq_relativa, freq_comulativa_assoluta,
                     freq_cumulativa_relativa, return_data_table=False):
    data_table = []
    for i in range(len(modalita)):
        data_table.append([i + 1, modalita[i], freq_assoluta[i], freq_relativa[i], freq_comulativa_assoluta[i],
                           freq_cumulativa_relativa[i]])

    print(pd.DataFrame(data_table, columns=['i', 'v_i', 'f_i', 'p_i', 'F_i', 'P_i']).to_string(index=False))

    if return_data_table:
        return data_table
