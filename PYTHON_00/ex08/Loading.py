# pyright: reportReturnType=false, reportInvalidTypeForm=false
import os

interval = 0.1  # in seconds
terminal_size = os.get_terminal_size().columns


def get_formated_time(seconds):
    return f"{int(seconds / 60):02d}:{int(seconds):02d}"


def get_stats(index, total_iterations, elapsed_time):
    iterations_per_second = index / elapsed_time
    eta_time = (total_iterations - index) / iterations_per_second

    return f"{index + 1}/{total_iterations} [{get_formated_time(elapsed_time)}<{get_formated_time(eta_time)}, {iterations_per_second:.2f}it/s]"


def display_progress(progress, stats):
    progress_bar = ""
    pourcentage = f"{progress:3.0f}%"
    bar_size = terminal_size - len(stats) - len(pourcentage) - 3

    for tile in range(bar_size):
        if (tile * 100) / (bar_size - 1) <= progress:
            progress_bar += "█"
        else:
            progress_bar += " "

    print(f"\r{pourcentage}|{progress_bar}| {stats}", end="")


def ft_tqdm(progress_iterable: range) -> None:
    start_time = os.times().elapsed
    last_update = os.times().elapsed
    total_iterations = len(progress_iterable)

    for index, iterator in enumerate(progress_iterable, start=1):
        current_time = os.times().elapsed
        progress = (index * 100) / (total_iterations - 1)

        if (
            current_time - last_update >= interval
            or index == 0
            or index == total_iterations - 1
        ):
            stats = get_stats(index, total_iterations, current_time - start_time)
            display_progress(progress, stats)

            last_update = current_time

        yield iterator
