def test_accumulator():
    amounts = [500, 1500, 200]
    assert sum(amounts) == 2200


def test_flag_filter():
    records = [{"amount": 500}, {"amount": 1500}, {"amount": 800}]
    flagged = [r for r in records if r["amount"] > 1000]
    assert len(flagged) == 1


def test_status_filter():
    records = [{"status": "Pending"}, {"status": "Approved"}]
    pending = [r for r in records if r["status"] == "Pending"]
    assert len(pending) == 1


def test_high_value():
    records = [{"amount": 2200}, {"amount": 1200}, {"amount": 3500}]
    high = [r for r in records if r["amount"] > 2000]
    assert len(high) == 2


def test_dict_access():
    rec = {"name": "Ransom", "amount": 750}
    assert rec["amount"] == 750
