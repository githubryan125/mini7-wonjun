from django.contrib import admin
from .models import TalkItem

class TimeFilter(admin.SimpleListFilter):
    title = 'Time'  # 필터 제목
    parameter_name = 'time'  # URL 매개변수 이름

    def lookups(self, request, model_admin):
        # 필터 옵션 정의
        return (
            ('morning', 'Morning'),
            ('afternoon', 'Afternoon'),
            ('evening', 'Evening'),
        )

    def queryset(self, request, queryset):
        # 필터링 로직 구현
        if self.value() == 'morning':
            return queryset.filter(time__hour__lt=12)
        elif self.value() == 'afternoon':
            return queryset.filter(time__hour__range=[12, 17])
        elif self.value() == 'evening':
            return queryset.filter(time__hour__gte=17)
        return queryset

@admin.register(TalkItem)
class TalkItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'time')
    list_filter = (TimeFilter,)  # 커스텀 필터 추가
