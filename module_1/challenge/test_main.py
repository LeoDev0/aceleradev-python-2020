from main import classify_by_phone_number, records


class TestChallenge1:

    def test_len(self):
        result = classify_by_phone_number(records)
        assert len(result) == 6
