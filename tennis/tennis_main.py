from tennis_game_class import Tennis

if __name__ == '__main__':
    match_seeds = [1010, 2020, 3030]

    for i, match_seed in enumerate(match_seeds):
        print(f"\nMatch #{i+1}")
        match = Tennis(match_seed)
        match.play()
        print("")

