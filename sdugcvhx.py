def main():
    champions = {}


    with open("world_cup_champions.txt", "r") as file:
     
        next(file)

        for line in file:
            line = line.strip()
            if not line:
                continue 

            parts = line.split(",")
            year = parts[0].strip()
            country = parts[1].strip()

            if country not in champions:
                champions[country] = []
            champions[country].append(year)


    print("FIFA World Cup Winners (Alphabetical)")
    print("-" * 40)
    for country in sorted(champions.keys()):
        years_won = ", ".join(champions[country])
        win_count = len(champions[country])
        print(f"{country} ({win_count}): {years_won}")

    most_wins_country = ""
    max_wins = 0

    for country, years in champions.items():
        if len(years) > max_wins:
            max_wins = len(years)
            most_wins_country = country

    print("-" * 40)
    print(f"Most championships: {most_wins_country} with {max_wins} wins")


if __name__ == "__main__":
    main()