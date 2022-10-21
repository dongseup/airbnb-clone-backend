from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class IsGoodReview(admin.SimpleListFilter):
    title = "점수별 리뷰 보기"

    parameter_name = "isGood"

    def lookups(self, request, model_admin):
        return [
            ("goodReview", "좋은리뷰(3점 이상)"),
            ("badReview", "나쁜리뷰(3점 미만)"),
        ]

    def queryset(self, request, reviews):
        isGood = self.value()
        print(reviews)
        if isGood:
            return (
                reviews.filter(rating__gte=3)
                if isGood == "goodReview"
                else reviews.filter(rating__lt=3)
            )
        else:
            return reviews


@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        IsGoodReview,
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
