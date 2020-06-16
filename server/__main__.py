from server.server import Server


def main() -> None:
    server = Server(__file__)
    server.run(ip='127.0.0.1', port=5555)


if __name__ == "__main__":
    main()
