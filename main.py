import time
import matplotlib.pyplot as plt
from regineBacktracking import n_queens_backtracking
from Lee import lee_algorithm
from regineAlpinist import hill_climbing
from regineAlpinist import print_board
from comis_voiajor import comis_voiajor
from comis_voiajor import citeste_date_intrare
from calirea_simulata import cautare_simulata
from calirea_simulata import numar_conflicte
from comis_voiajor_genetic import City
from comis_voiajor_genetic import comis_voiajor_genetic


def main():
    execution_times = []
    while True:
        print("Meniu:")
        print("1. ALG Lee (lab 1)")
        print("2. N Regine cu alpinist (lab 6)")
        print("3. Comis voiajor (lab 7)")
        print("4. N regine cu călire simulată (lab 8)")
        print("5. Comis voiajor algoritm genetic (lab 9)")
        print("6. Grafic cu variația timpului de execuție")
        print("7. Informații despre autor")
        print("8. Ieșire")

        option = input("Selectați o opțiune: ")

        if option == "1":

            import time
            start_time = time.time()
            matrix = [
                [0, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 1, 0]
            ]
            start = (0, 0)
            end = (3, 3)
            shortest_path = lee_algorithm(matrix, start, end)
            print(shortest_path)
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)

            file = open("outputLEE.txt", "w")

            elapsed_time_str = str(elapsed_time)
            # Write the string to the file
            file.write(elapsed_time_str)

            path_str = ' '.join(map(str, shortest_path))
            # Write the string to the file
            file.write(path_str)
            file.close()

        elif option == "2":

            file = open("outputALPINIST.txt", "w")

            start_time = time.time()
            solution = hill_climbing(8)
            print(solution)
            print_board(solution)
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)
            path_str = ' '.join(map(str, solution))
            # Write the string to the file
            file.write(path_str)
            file.write(str(elapsed_time))


            solution = hill_climbing(16)
            print(solution)
            print_board(solution)
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)
            path_str = ' '.join(map(str, solution))
            # Write the string to the file
            file.write(path_str)
            file.write(str(elapsed_time))


            solution = hill_climbing(32)
            print(solution)
            path_str = ' '.join(map(str, solution))
            # Write the string to the file
            file.write(path_str)
            file.write(str(elapsed_time))
            # print_board(solution)
            # solution = hill_climbing(64)
            # print(solution)
            # print_board(solution)
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)

            path_str = ' '.join(map(str, solution))
            # Write the string to the file
            file.write(path_str)
            file.write(str(elapsed_time))
            file.close()

        elif option == "3":

            start_time = time.time()
            file = open("outputComisVoiajor.txt", "w")
            n, orase, distante, start = citeste_date_intrare('comis_voiajor_input1.txt')
            if n is not None:
             comis_voiajor(n, orase, distante, start)
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)
            file.write(str(elapsed_time))
            start_time = time.time()
            n, orase, idstante, start = citeste_date_intrare('comis_voiajor_input1.txt')
            if n is not None:
             comis_voiajor(n, orase, distante, start)
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)
            file.write(str(elapsed_time))
            start_time = time.time()
            n, orase, distante, start = citeste_date_intrare('comis_voiajor_input1.txt')
            if n is not None:
             comis_voiajor(n, orase, distante, start)
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)
            file.write(str(elapsed_time))

            file.close()

        elif option == "4":

            file = open("outputCALIRE.txt", "w")
            n = int(input("Numarul pentru cautare simulata: "))
            start_time = time.time()
            stare_finala = cautare_simulata(n)
            print("Starea finală: ", stare_finala)
            print("Numărul de conflicte: ", numar_conflicte(stare_finala))
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)
            file.write(str(elapsed_time))

            n = int(input("Numarul pentru cautare simulata: "))
            start_time = time.time()
            stare_finala = cautare_simulata(n)
            print("Starea finală: ", stare_finala)
            print("Numărul de conflicte: ", numar_conflicte(stare_finala))
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)
            file.write(str(elapsed_time))

            n = int(input("Numarul pentru cautare simulata: "))
            start_time = time.time()
            stare_finala = cautare_simulata(n)
            print("Starea finală: ", stare_finala)
            print("Numărul de conflicte: ", numar_conflicte(stare_finala))
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)
            file.write(str(elapsed_time))
            file.close()

        elif option == "5":

            start_time = time.time()
            cities = [
                City(60, 200),
                City(180, 200),
                City(80, 180),
                City(140, 180),
                City(20, 160),
                City(100, 160),
                City(200, 160),
                City(140, 140),
                City(40, 120),
                City(100, 120),
                City(180, 100),
                City(60, 80),
                City(120, 80),
                City(180, 60),
                City(20, 40),
                City(100, 40),
                City(200, 40),
                City(20, 20),
                City(60, 20),
                City(160, 20)
            ]

            population_size = 100
            num_generations = 1000
            mutation_rate = 0.01

            best_tour = comis_voiajor_genetic(cities, population_size, num_generations, mutation_rate)
            best_tour.calculate_distance()

            file = open("outputCOMISVOIAJORGENETIC.txt", "w")

            print("Cea mai scurtă rută găsită:")
            for city in best_tour.cities:
                print(city.x, city.y)
                file.write(str(city.x) + "   ")
                file.write(str(city.y) + "\n")
            print("Distanta totala:", best_tour.distance)
            elapsed_time = time.time() - start_time
            execution_times.append(elapsed_time)
            file.write(str(elapsed_time))
            file.close()

        elif option == "6":
            
            x = range(1, len(execution_times) + 1)
            for i, time in enumerate(execution_times):
                plt.plot([i+1], [time], marker='o', label=f'Execution {i+1}')

            plt.xlabel('Execution Number')
            plt.ylabel('Execution Time (seconds)')
            plt.title('Variation of Execution Time')
            plt.legend()
            plt.show()
        elif option == "7":
            print("DASCALU SAMUEL 3131A")
        elif option == "8":
            break
        else:
            print("Opțiune invalidă. Selectați din nou.")

if __name__ == "__main__":
    main()