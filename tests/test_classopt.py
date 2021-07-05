import unittest
import sys

from classopt import ClassOpt, config


@ClassOpt
class Opt:
    arg_int: int
    arg_str: str
    arg_float: float


@ClassOpt()
class AdvancedUsageOpt:
    long_arg: str = config(long=True)
    short_arg1: str = config(long=True, short=True)
    short_arg2: str = config(long=True, short="-x")
    default_int: int = config(long=True, default=3)
    store_true: bool = config(long=True, action="store_true")
    nargs: list = config(long=True, nargs="+", type=int)


@ClassOpt(default_long=True)
class DefaultLongOpt:
    arg1: int
    arg2: str


@ClassOpt(default_long=True, default_short=True)
class DefaultShortOpt:
    a_arg: int
    b_arg: str


class TestClassOpt(unittest.TestCase):
    def test_classopt(self):
        set_args("5", "hello", "3.2")

        opt = Opt.from_args()

        assert opt.arg_int == 5
        assert opt.arg_str == "hello"
        assert opt.arg_float == 3.2

        del_args()

    def test_advanced_usage(self):
        set_args(
            "--long_arg",
            "long_arg",
            "-s",
            "short_arg1",
            "-x",
            "short_arg2",
            "--store_true",
            "--nargs",
            "1",
            "2",
            "3",
        )

        opt = AdvancedUsageOpt.from_args()

        assert opt.long_arg == "long_arg"
        assert opt.short_arg1 == "short_arg1"
        assert opt.short_arg2 == "short_arg2"
        assert opt.default_int == 3
        assert opt.store_true
        assert opt.nargs == [1, 2, 3]

        del_args()

    def test_default_long(self):
        set_args("--arg1", "3", "--arg2", "hello")

        opt = DefaultLongOpt.from_args()

        assert opt.arg1 == 3
        assert opt.arg2 == "hello"

        del_args()

    def test_default_short(self):
        set_args("-a", "3", "-b", "hello")

        opt = DefaultShortOpt.from_args()

        assert opt.a_arg == 3
        assert opt.b_arg == "hello"

        del_args()


def set_args(*args):
    for arg in args:
        sys.argv.append(arg)


def del_args():
    del sys.argv[1:]
