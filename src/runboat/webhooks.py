def on_pr_open_or_update() -> None:
    # find Repo
    # find image from target branch (exit if not found)
    # find or create Branch
    # create Build
    # start build (enqueue)
    ...


def on_pr_close_or_merge() -> None:
    # find Repo, Branch
    # delete branch (enqueue)
    ...


def on_push() -> None:
    # find Repo, branch
    # find image from target branch (exit if not found)
    # find or create Branch
    # create Build
    # start build (enqueue)
    ...
