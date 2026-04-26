from django.forms import TextInput


class MaskedWidget(TextInput):
    template_name = 'masked_input/masked_input.html'

    def __init__(self, mask, attrs=None):
        self.mask = mask
        self.display_length = len(mask)
        self.value_length = mask.count('0')
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        context['widget'].update(
            {
                'mask': self.mask,
                'display_length': self.display_length,
                'value_length': self.value_length,
                'value': value,
            }
        )
        return context
