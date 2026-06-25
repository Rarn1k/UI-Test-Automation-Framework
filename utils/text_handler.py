class TextHandler:

    @staticmethod
    def get_num_from_text(text: str) -> int:
        digits = filter(lambda ch: ch.isdigit(), text)
        return int(''.join(digits))