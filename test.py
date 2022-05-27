from funzioni import *

elements = [2, 7, 4, 2, 4, 5, 2, 4, 5, 3, 7, 6, 3, 2, 4, 6, 5, 6, 4, 5, 5, 5, 4, 8, 5, 6, 5,
            3, 3, 4, 2, 3, 3, 5, 4, 7, 3, 2, 3, 6, 3, 4, 4, 2, 5, 4, 2, 4, 5, 4, 2, 5, 4, 3,
            4, 7, 4, 6, 8, 4, 7, 4, 4, 8, 2, 4, 6, 3, 6, 4, 2, 4, 3, 6, 5, 4, 5, 4, 3, 5]

n = len(elements)

modalita = modalita_del_carattere(elements)
freq_assoluta = frequenza_assoluta(elements)
freq_comulativa_assoluta = frequenzaa_comulativa_assoluta(freq_assoluta)
freq_relativa = frequeza_relativa(n, freq_assoluta)
freq_cumulativa_relativa = frequenza_cumulativa_relativa(n, freq_comulativa_assoluta)

print_data_table(modalita, freq_assoluta, freq_relativa, freq_comulativa_assoluta, freq_cumulativa_relativa)
