def get_max_objects_in_the_area(desk_length: int, width: int, height: int):
    objects_per_row = desk_length // width
    max_rows = desk_length // height
    return objects_per_row * max_rows


def get_min_desk_length(n: int, width: int, height: int):
    if all([
        1 <= n <= 1012,
        1 <= width <= 109,
        1 <= height <= 109,
    ]):
        min_desk_length = 1
        desk_length = height * n if height >= width else width * n

        while min_desk_length < desk_length:
            mid = (desk_length + min_desk_length) // 2

            if get_max_objects_in_the_area(mid, width, height) >= n:
                desk_length = mid
                continue
            min_desk_length = mid + 1

        return min_desk_length
    return -1
