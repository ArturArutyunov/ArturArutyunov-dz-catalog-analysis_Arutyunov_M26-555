import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    """Возвращает среднюю оценку по каталогу"""
    if not movies:
        return 0.0
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (возраст самого старого фильма,
    возраст самого нового, средний возраст)"""
    if not movies:
        return (0, 0, 0)

    years = [movie["year"] for movie in movies]
    oldest_year = current_year - min(years)
    newest_year = current_year - max(years)

    average_age = math.ceil(current_year - sum(years) / len(years))

    return (oldest_year, newest_year, average_age)

def duration_in_hours(minutes):
    """Переводит минуты в формат '2ч 35м'."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

def rating_tier(rating):
    """Возвращает категорию по оценке"""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    """Возвращает метку: новые / недавние / старые"""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"


non_comedies = []
for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    non_comedies.append(movie["title"])

if non_comedies:
    print("Фильмы не относящиеся к жанру comedy:")
    for title in non_comedies:
        print(f"  {title}")

current = 0
while current < len(movies):
    if movies[current]["rating"] > 9.0:
        print(f"\nФильм-шедевр: {movies[current]['title']}")
        break
    current += 1
else:
    print("\nШедевров не найдено")

def count_long_movies(movies, threshold=120):
    """Считает фильмы длиннее threshold"""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title):
    """Приводит строку к Title Case"""
    words = title.split()
    normalized = [word[0].upper() + word[1:] for word in words]
    return " ".join(normalized)

def make_slug(title):
    """Превращает нормализованное название в слаг"""
    normalized = normalize_title(title)
    return normalized.lower().replace(" ", "-")

def format_report_line(movie):
    """Возвращает единую строку с описанием фильма."""
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{title}" ({movie["year"]}) - {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )

def titles_sorted_by_rating(movies):
    """Возвращает список названий, отсортированных по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    """Возвращает список из топ n кортежей (title, rating)"""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

def count_by_genre(movies):
    """Возвращает словарь {жанр: количество фильмов}"""
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def actor_filmography(movies):
    """Возвращает cловарь {актёр: [список названий фильмов]}"""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, []) + [movie["title"]]
    return filmography


def get_above_average(movies):
    """Возвращает cловарь фильмов с рейтингом выше среднего"""
    average = average_rating(movies)
    above_average = {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average
    }
    return above_average

def all_genres(movies):
    """Возвращает множество уникальных жанров"""
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres

def common_actors(movie1, movie2):
    """Возвращает множество актеров, снимавшихся в обоих фильмах"""
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    """Возвращает жанры, встречающиеся в movies_a, но не встречающиеся в movies_b"""
    return all_genres(movies_a) - all_genres(movies_b)

def iter_high_rated(movies, min_rating=8.0):
    """Лениво отдаёт фильмы с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

print("\nФильмы с рейтингом ≥ 7:")
for i, movie in enumerate(iter_high_rated(movies, 7), start=1):
    print(f"  {i}. {format_report_line(movie)}")

total_minutes = sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)
print(f"\nСуммарная длительность фильмов с рейтингом > 7: {total_minutes} мин\n")


def build_report(movies):
    """Выводит отчёт по каталогу фильмов"""
    if not movies:
        print("Каталог пуст")
        return

    average = average_rating(movies)
    _, _, average_age = catalog_age_stats(movies)

    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average}")
    print(f"Средний возраст фильмов: {average_age} лет")
    print()

    print("Топ-3 фильма:")
    for title, _ in top_n_by_rating(movies, 3):
        movie = next(m for m in movies if m["title"] == title)
        print(f"  {format_report_line(movie)}")
    print()

    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    for genre, count in sorted(
        genre_counts.items(), key=lambda item: item[1], reverse=True
    ):
        print(f"  {genre} — {count}")
    print()

    genres = all_genres(movies)
    print(f"Все жанры каталога: {', '.join(sorted(genres))}")


if __name__ == "__main__":
    build_report(movies)