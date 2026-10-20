
from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


def test_days_left_counts_days_until_due():
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    result = days_left(due, today)
    assert result == 4


# TODO 1
def test_days_left_is_negative_when_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 17)
    result = days_left(due, today)
    assert result == -2


# TODO 2
def test_is_urgent_when_due_tomorrow():
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)
    assert is_urgent(due, today) is True


# TODO 3
def test_is_urgent_when_due_in_exactly_two_days():
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)
    assert is_urgent(due, today) is True


# TODO 4
def test_is_urgent_when_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 18)
    assert is_urgent(due, today) is False


# TODO 5
def test_sort_by_due_puts_soonest_first():
    tasks = [
        {"title": "Task C", "due": date(2026, 10, 25)},
        {"title": "Task A", "due": date(2026, 10, 20)},
        {"title": "Task B", "due": date(2026, 10, 22)},
    ]
    result = sort_by_due(tasks)
    assert result[0]["title"] == "Task A"


# TODO 6
def test_completion_rate_is_zero_when_no_tasks():
    result = completion_rate(0, 0)
    assert result == 0.0


# TODO 7
def test_completion_rate_returns_33_3():
    result = completion_rate(1, 3)
    assert result == 33.3
