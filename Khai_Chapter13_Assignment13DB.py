# In this assignment, I am creating a table to show the population of 10 florida cities of my choice, showing their population, the year the population was recorded, and changes over 20 years.



import sqlite3
import matplotlib.pyplot as plt

# Database setup
def create_database():
    conn = sqlite3.connect('population_kb.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Insert data for year and population
def insert_initial_data():
    conn = sqlite3.connect('population_kb.db')
    cursor = conn.cursor()
    cities = [
        ('Orlando', 2023, 280000),
        ('Tampa', 2023, 400000),
        ('Sarasota', 2023, 57000),
        ('Palmetto', 2023, 14000),
        ('Miami', 2023, 500000),
        ('St. Petersburg', 2023, 260000),
        ('Hollywood', 2023, 153000),
        ('Venice', 2023, 25000),
        ('Naples', 2023, 22000),
        ('Destin', 2023, 14000)
    ]
    cursor.executemany('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', cities)
    conn.commit()
    conn.close()

# Simulate population growth for 20 years
def simulate_population_growth():
    conn = sqlite3.connect('population_kb.db')
    cursor = conn.cursor()
    cursor.execute('SELECT city, population FROM population WHERE year = 2023')
    initial_data = cursor.fetchall()

    for city, population in initial_data:
        for year in range(2024, 2044):
            population = int(population * 1.02)  # 2% growth per year
            cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, year, population))
    conn.commit()
    conn.close()

# Show population growth for city
def plot_population_growth():
    conn = sqlite3.connect('population_kb.db')
    cursor = conn.cursor()

    while True:
        # Display results
        cursor.execute('SELECT DISTINCT city FROM population')
        cities = [city[0] for city in cursor.fetchall()]
        print("\nAvailable Cities:")
        for i, city in enumerate(cities):
            print(f"{i + 1}. {city}")

        choice = input("Choose a city by entering the corresponding number (type 'SEND' to exit): ")
        if choice.lower() == 'SEND':
            break

        try:
            city_index = int(choice) - 1
            if 0 <= city_index < len(cities):
                selected_city = cities[city_index]
                cursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (selected_city,))
                data = cursor.fetchall()

                years = [row[0] for row in data]
                populations = [row[1] for row in data]

                plt.figure(figsize=(10, 6))
                plt.plot(years, populations, marker='o')
                plt.title(f"Population Growth of {selected_city} (2023-2043)")
                plt.xlabel("Year")
                plt.ylabel("Population")
                plt.grid()
                plt.show()
            else:
                print("Invalid Input. Select a valid city number.")
        except ValueError:
            print("Invalid input. Enter a number or 'SEND'.")

    conn.close()


if __name__ == "__main__":
    create_database()
    insert_initial_data()
    simulate_population_growth()
    plot_population_growth()
