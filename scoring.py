from model import Library


def total_score_library(library: Library):
    total = 0
    for i in library.book_list:
        total += i.score
    return total


def efficiency_library(library: Library, remaining_days_total):
    # calcul du nombre de jour nécéssaire pour écouler tous les livres de la lib
    total_days_library = (library.number_of_books / library.books_per_day )
    # si le nombre de jour necéssaire est inf au nombre de jour restant (en comptant le temps de signup)
    if total_days_library < remaining_days_total - library.sign_up_days:
        return efficiency_remaining_days(remaining_days_total - library.sign_up_days, library) / (total_days_library + library.sign_up_days)
    else:
        return total_score_library(library) / (remaining_days_total + library.sign_up_days)


def efficiency_remaining_days(days_to_scan: int, library: Library):
    score = 0
    books_scanned = days_to_scan * library.books_per_day
    list_books = library.book_list
    for i in range(books_scanned):
        if i < len(list_books):
            score += list_books[i].score
        else:
            return score


def efficiency_on_given_days(days: int, library: Library):
    return efficiency_remaining_days(days, library)
