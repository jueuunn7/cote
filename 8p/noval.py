def has_seven(n: int) -> bool:
    if n <= 0:
        return False
    elif n % 7 == 0:
        return True
    elif n % 10 == 7:
        return True
    return has_seven(n // 10)

def pingpong(n: int, cnt: int = 1, value: int = 1, direction: int = 1) -> None:
    if n == cnt:
        print(value)
        return

    pingpong(
        n=n,
        cnt=cnt + 1,
        value=value-direction if has_seven(cnt) else value + direction,
        direction=-direction if has_seven(cnt) else direction
    )

pingpong(100)