from django.views.generic.edit import FormView
import MeCab
from . import forms
from collections import Counter


class Index(FormView):
    form_class = forms.TextForm
    template_name = "index.html"
    
    def form_valid(self, form):
        data = form.cleaned_data
        text = data["text"]
        tagger = MeCab.Tagger()
        parsed_txt = tagger.parse(text)
        elements = parsed_txt.split('\n')[:-2]
        matome=[]
        for element in elements:
            parts = element.split(',')
            aaa = parts[0].split('\t')
            pos = aaa[4]
            
            matome.append(pos)
        result = str(Counter(matome))[9:-2]
                      
        ctxt = self.get_context_data(result=result)
        return self.render_to_response(ctxt)
