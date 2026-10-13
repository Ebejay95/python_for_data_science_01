def print_progress(current: int, total: int) -> None:
    """Display the progress bar for current out of total iterations."""
    width = 64
    percent = current * 100 // total
    filled = current * width // total
    bar = ("=" * (filled - 1) + ">") if filled > 0 else ""
    print(f"\r{percent:3d}%|[{bar:<{width}}]| {current}/{total}",
          end="", flush=True)


def ft_tqdm(lst: range) -> None:
    """Yield each element of lst while displaying a progress bar,
    like tqdm."""
    total = len(lst)
    if total == 0:
        return
    print_progress(0, total)
    for index, elem in enumerate(lst, 1):
        yield elem
        print_progress(index, total)


def main():
    """Nothing to run, ft_tqdm is meant to be imported."""
    return


if __name__ == "__main__":
    main()
