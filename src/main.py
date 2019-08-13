from times import Times
import argparse

ts = Times()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Memorize your minutes")

    subparsers = parser.add_subparsers()
    parser_post = subparsers.add_parser("post")
    parser_post.add_argument("message", type=str, help="message")

    parser_recall = subparsers.add_parser("show")
    parser_recall.add_argument("show", type=int, help="display num")

    args = parser.parse_args()

    if hasattr(args, "message"):
        ts.post(args.message)
    elif hasattr(args, "show"):
        ts.recall(args.show)
    else:
        raise ValueError()
