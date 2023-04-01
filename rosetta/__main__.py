from rosetta import api, cli, utils


def main():
    args = cli.cli()
    payload = utils.mount_payload(args.i, args.o, args.t)
    response: dict | str = api.post_translate(payload)
    if isinstance(response, dict):
        text = utils.parse_response(response)
    else:
        text = response
    print(text)


if __name__ == "__main__":
    main()
