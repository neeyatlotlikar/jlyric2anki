from rich.progress import Progress, SpinnerColumn, TextColumn


def show_loader(task_description: str, func, *args, **kwargs):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(task_description, start=False)
        progress.start_task(task)
        result = func(*args, **kwargs)
        progress.update(task, completed=100)
    return result
