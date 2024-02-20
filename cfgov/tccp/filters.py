from django import forms

from django_filters import rest_framework as filters


class CardOrderingFilter(filters.OrderingFilter):
    def __init__(self, *args, **kwargs):
        kwargs.update(
            {
                "choices": [
                    ("purchase_apr", "Lowest purchase APR"),
                    ("transfer_apr", "Lowest balance transfer APR"),
                    ("low_fees", "Lowest fees"),
                ],
                "initial": "purchase_apr",
            }
        )
        super().__init__(*args, **kwargs)

    def filter(self, qs, value):
        # If "low_fees" is selected, order first by cards without late fees
        # (boolean), then by first late fee in dollars, in ascending order.
        if value[0] == "low_fees":
            return qs.order_by("late_fees", "late_fee_dollars")

        # Otherwise, if we're sorting by APR, we want to exclude any cards
        # that don't specify an APR.
        qs = qs.exclude(**{f"{value[0]}__isnull": True})

        return super().filter(qs, value)


class CheckboxFilter(filters.BooleanFilter):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault(
            "widget", forms.CheckboxInput(attrs={"class": "a-checkbox"})
        )
        super().__init__(*args, **kwargs)

    def filter(self, qs, value):
        return super().filter(qs, True) if value else qs
