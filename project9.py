import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv("movies.csv")
ratings = pd . read_csv("ratings.csv")

movie_data = pd.merge(ratings,movies,on="movieId")
print("==== MOVIE DATASET ANALYSIS====")

while True:
    print("\n ==== Menu ====")
    print("1. view dataset")
    print("2. Top 10 most rated movies")
    print("3. Top 10 Highest rated movies")
    print("4. Rating statistics")
    print("5. genre analysis")
    print("6. Rating Distribution Graph")
    print("7. movie recommandation")
    print("8. EXit")

    choice = input("enter your choice:")

    if choice == "1":
        print(movie_data.head())

    elif choice == "2":
        most_rated = movie_data.groupby("title")["rating"].count()
        print("\n Top 10 most rated movies:")
        print(most_rated.sort_values(ascending=False).head(10))

    elif choice == "3":
        highest_rated = movie_data.groupby("title")["rating"].mean()
        print("\n Top 10 Highest Rated Movies:")
        print(highest_rated.sort_values(ascending=False).head(10))

    elif choice == "4":
        print("\n Rating statistics:")
        print(movie_data["rating"].describe())

    elif choice == "5":
        genre_count = movies["genres"].value_counts()
        print("\n Top genres:")
        print(genre_count.head(10))

    elif choice == "6":
        plt.figure(figsize=(8,5))
        movie_data["rating"].hist(bins=10)
        plt.title("rating distribution")
        plt.xlabel("rating")
        plt.ylabel("frequency")
        plt.show()

    elif choice == "7":
        movie_matrix = movie_data.pivot_table(
            index = "userId",
            columns = "title",
            values = "rating"
        )
        
        movie_name = input("enter mmovie name exactly:")

        if movie_name in movie_matrix.columns:
            similar_movies = movie_matrix.corrwith(
                movie_matrix[movie_name]
            )

            recommendations = pd.DataFrame(
                similar_movies,
                columns = ["correlation"]
            )

            recommendations.dropna(inplace=True)
            
            print("recommended Movies:")
            print(
                recommendations
                .sort_values("correlation", ascending = False)
                .head(10)
            )

        else:
            print("Movie not found!")

    elif choice == "8":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")