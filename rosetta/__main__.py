from rosetta import api, cli, utils


def main():
    args = cli.cli()
    payload = utils.mount_payload(args.input_language, args.output_language, args.text)
    response: dict | str = api.post_translate(payload)
    if isinstance(response, dict):
        text = utils.parse_response(response)
    else:
        text = response
    print(text)


if __name__ == "__main__":
    main()
