from django.utils.translation import gettext_lazy as _


class PostsDataMixin:
    paginate_by = 8
    title = None
    extra_context = {}

    def __init__(self):
        if self.title:
            self.extra_context['title'] = _(self.title)

    def get_mixin_context(self, context: dict, **kwargs):
        if context['title'] is None:
            context['title'] = self.extra_context['title']
        context.update(kwargs)
        return context


# Замена русских букв на английские буквы для слагов
def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'eh', 'ю': 'yu', 'я': 'ya'}

    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))