from rosetta import api, cli, utils


def main():
    args = cli.cli()
    payload = utils.mount_payload(args.i, args.o, args.t)
    response = api.post_translate(payload)
    text = utils.parse_response(response)
    print(text)



if __name__ == "__main__":
    main()
