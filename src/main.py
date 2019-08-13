from times import Times
import argparse


def main():
    ts = Times()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Memorize your minutes")

    parser.add_argument(
        "query_type", const="post", nargs="?", default="post", choices=["post", "show"]
    )
    args = parser.parse_args()
    query_type = args.query_type

    if query_type == "post":
        pass
    elif query_type == "show":
        pass
    else:
        raise AssertionError
