import pytest

from pixler import OutOfBoundsException, Pixler


def test_pixler_dot_1() -> None:
    pixler = Pixler.from_pixels([[1, 0], [0, 0], [0, 0], [0, 0]])
    assert pixler.get_frame() == "⠁"


def test_pixler_dot_2() -> None:
    pixler = Pixler.from_pixels([[0, 0], [1, 0], [0, 0], [0, 0]])
    assert pixler.get_frame() == "⠂"


def test_pixler_dot_3() -> None:
    pixler = Pixler.from_pixels([[0, 0], [0, 0], [1, 0], [0, 0]])
    assert pixler.get_frame() == "⠄"


def test_pixler_dot_4() -> None:
    pixler = Pixler.from_pixels([[0, 1], [0, 0], [0, 0], [0, 0]])
    assert pixler.get_frame() == "⠈"


def test_pixler_dot_5() -> None:
    pixler = Pixler.from_pixels([[0, 0], [0, 1], [0, 0], [0, 0]])
    assert pixler.get_frame() == "⠐"


def test_pixler_dot_6() -> None:
    pixler = Pixler.from_pixels([[0, 0], [0, 0], [0, 1], [0, 0]])
    assert pixler.get_frame() == "⠠"


def test_pixler_dot_7() -> None:
    pixler = Pixler.from_pixels([[0, 0], [0, 0], [0, 0], [1, 0]])
    assert pixler.get_frame() == "⡀"


def test_pixler_dot_8() -> None:
    pixler = Pixler.from_pixels([[0, 0], [0, 0], [0, 0], [0, 1]])
    assert pixler.get_frame() == "⢀"


def test_pixler_dot_1358() -> None:
    pixler = Pixler.from_pixels([[1, 0], [0, 1], [1, 0], [0, 1]])
    assert pixler.get_frame() == "⢕"


def test_pixler_filled() -> None:
    pixler = Pixler.from_pixels([[1, 1], [1, 1], [1, 1], [1, 1]])
    assert pixler.get_frame() == "⣿"


def test_pixler_empty() -> None:
    pixler = Pixler.from_pixels([[0, 0], [0, 0], [0, 0], [0, 0]])
    assert pixler.get_frame() == "⠀"


def test_pixler_set_pixel() -> None:
    pixler = Pixler(2, 4)
    assert pixler.get_frame() == "⠀"

    pixler.set_pixel(0, 0, True)
    assert pixler.get_frame() == "⠁"

    pixler.set_pixel(1, 0, True)
    assert pixler.get_frame() == "⠉"

    pixler.set_pixel(0, 0, False)
    assert pixler.get_frame() == "⠈"

    pixler.set_pixel(1, 0, False)
    assert pixler.get_frame() == "⠀"


def test_pixler_set_pixel_out_of_bounds() -> None:
    pixler = Pixler(2, 4)

    pixler.set_pixel(0, 0)
    pixler.set_pixel(1, 0)

    with pytest.raises(OutOfBoundsException):
        pixler.set_pixel(2, 0)


def test_pixler_two_columns() -> None:
    pixler = Pixler.from_pixels(
        [[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1]]
    )
    assert pixler.get_frame() == "⢣⢕"


def test_pixler_two_rows() -> None:
    pixler = Pixler.from_pixels(
        [[1, 0], [1, 0], [0, 1], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1]]
    )
    assert pixler.get_frame() == "⢣\n⢕"


def test_pixler_diagonal() -> None:
    pixler = Pixler.from_pixels(
        [
            [1, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 1],
        ]
    )
    # fmt: off
    assert pixler.get_frame() == "\n".join([
        "⠑⢄⡠⠊",
        "⡠⠊⠑⢄",
    ])
    # fmt: on


def test_pixler_globe() -> None:
    pixel_map = [
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    pixler = Pixler.from_pixels(pixel_map)
    # fmt: off
    assert pixler.get_frame() == "\n".join([
        "⠀⢠⠒⣉⠕⢲⢉⠆",
        "⢀⢗⠉⠀⠀⢀⠇⠀",
        "⠣⠬⠒⠤⠔⠊⠀⠀",
    ])
    # fmt: on
