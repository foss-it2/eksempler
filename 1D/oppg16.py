"""
Lag et program med en løkke som samtidig finner største og minste verdi i en liste. 
Test programmet og kontroller det ved å bruke min() og max() i tillegg.
"""
from random import randint

def finn_min_maks(liste):
    # Finner maks og min samtidig
    minst = liste[0]
    maks = liste[0]
    for tall in liste:
        if tall < minst:
            minst = tall
        elif tall > maks:
            maks = tall
    return minst,maks

def innebygget(liste):
    return min(liste), max(liste)


if __name__ == "__main__":
    import timeit
    N = 10000000
    liste = [randint(1,1000) for x in range(1,21)]
    # Measure the execution time of my_function
    execution_time = timeit.timeit("finn_min_maks(liste)", globals=globals(), number=N)
    print(f"Execution time Henriks funksjon: {execution_time:.6f} seconds")
    execution_time2 = timeit.timeit("innebygget(liste)", globals=globals(), number=N)
    print(f"Execution time min()/maks() innebygde funksjoner: {execution_time2:.6f} seconds")
    
    minst,maks = finn_min_maks(liste)
    print(f"Min: {min(liste)}, maks: {max(liste)}")
    print(f"Min: {minst}, maks: {maks}")

