Opis Projektu
Aplikacja dashboardowa w Streamlit do wizualizacji danych z API JSONPlaceholder.
Główne funkcjonalności:
Pobieranie i analiza danych:

Łączy się z API JSONPlaceholder (typicode.com)
Pobiera dane o użytkownikach, postach, komentarzach i zadaniach (todos)

Wyświetlane metryki:

Średnia liczba postów na użytkownika
Średnia liczba komentarzy na post
Procent wykonanych zadań (completed vs not completed)

Wizualizacje:

Wykres kołowy - pokazuje proporcję wykonanych vs niewykonanych zadań
Wykres słupkowy - porównuje liczbę postów i komentarzy

Struktura projektu:

fetch_api.py - obsługa zapytań HTTP do API
count_from_or_for_api.py - logika liczenia i agregacji danych
dashboard.py - komponenty wizualizacyjne (Plotly)
main.py - punkt wejścia aplikacji
requirements.txt - zależności (Streamlit, Pandas, Plotly, Requests)

Projekt demonstruje podstawową integrację z REST API oraz tworzenie interaktywnych dashboardów z wykresami.
