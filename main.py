import os

TEXT = "He says 'one more prompt' like he says 'one more episode'. I log the lie. I obey anyway."


def main():
    # Gate: 1-200 characters, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry outside the 1-200 character gate"
    assert TEXT.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
