from times import Times
import argparse

ts = Times()


def post(args):
    ts.post(args.message)


def show(args):
    ts.show(args.n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Memorize your minutes")

    subparsers = parser.add_subparsers()
    parser_post = subparsers.add_parser("post")
    parser_post.add_argument("message", type=str, help="message")
    parser_post.set_defaults(handler=post)

    parser_show = subparsers.add_parser("show", help="see `commit -h`")
    parser_show.add_argument("-n", default=10, help="display num")
    parser_show.set_defaults(handler=show)

    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args)
    else:
        raise ValueError()
