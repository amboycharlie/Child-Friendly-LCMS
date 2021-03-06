
from leonardo.views import ModalFormView
from leonardo.forms import SelfHandlingForm


class FakeForm(SelfHandlingForm):

    def handle(self, request, data):
        pass


class ModalIframeView(ModalFormView):

    form_class = FakeForm

    template_name = 'devel/modal_iframe.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ModalFormView, self).get_context_data(*args, **kwargs)

        context['url'] = self.kwargs['url'] + '?_popup=1'
        context['modal_size'] = 'lg'
        return context
