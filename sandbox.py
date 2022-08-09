from classopt import classopt, config
import argparse

@classopt(parser_factory=argparse.ArgumentParser)
class Opt:
    arg_int: int
    arg_str: str
    arg_float: float

opt2 = Opt.from_args("5","hello","3.2")

