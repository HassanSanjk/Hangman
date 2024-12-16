class file_utils:
    @staticmethod
    def read_words(file_name = "words.txt"):
        words = {}
        try:
            with open(file_name, "r") as file:
                for line in file:
                    word, hint = line.strip().split(",", 1)
                    if word in words:
                        print(f"Duplicate word: {word}")
                    words[word] = hint
        except FileNotFoundError:
            print("Error: Data file not found.")
        except Exception as e:
            print(f"Error reading data file: {e}")
        return words

    @staticmethod
    def read_leaderboard(file_name = "leaderboard.txt"):
        leaderboard = {}
        try:
            with open(file_name, "r") as file:
                for line in file:
                    name, score = line.strip().split(",", 1)
                    score = int(score)
                    if name in leaderboard:
                        print(f"Duplicate name: {name}")
                    leaderboard[name] = score
        except FileNotFoundError:
            print("Error: Data file not found.")
        except Exception as e:
            print(f"Error reading data file: {e}")
        return leaderboard

    @staticmethod
    def update_leaderboard(leaderboard,name,score, file_name = "leaderboard.txt"):
        if name not in leaderboard or score > leaderboard[name]:
            leaderboard[name] = score
            print(f"New higscore for {name}: {score}")
        else:
            print("You did not beat your previous highscore of", leaderboard[name])
        try:
            with open(file_name, "w") as file:
                for leaderboard_name, leaderboard_score in leaderboard.items():
                    file.write(f"{leaderboard_name},{leaderboard_score}\n")
        except FileNotFoundError:
            print("Error: Data file not found.")
        except Exception as e:
            print(f"Error writing data file: {e}")
