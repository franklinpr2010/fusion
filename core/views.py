from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario
from .forms import ContatoForm

#vai herdar do formView porque vem do formulário
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    #depois de sucesso envia ao index
    success_url = reverse_lazy('index')

 #vai recuperar o contexto e adicionar dados dentro dele
    def get_context_data(self, **kwargs):
        #recuperando o contexto, tinha alguma coisa no contexto da página, se tinha foi recuperado
        context = super(IndexView, self).get_context_data(**kwargs)
        #Colocando no contexto todos os servicos
        #ordena por qualquer campo que for informado
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)