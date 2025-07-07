import pandas as pd
import io, base64
from django.views.generic import TemplateView
from .forms import CsvUploadForm
import matplotlib.pyplot as plt

class CsvUploadAndResultView(TemplateView):
    template_name = 'kashika/upload.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'form': CsvUploadForm()})

    def post(self, request, *args, **kwargs):
        form = CsvUploadForm(request.POST, request.FILES)
        context = {'form': form}

        if form.is_valid():
            file = form.cleaned_data['file']
            content = file.read().decode('utf-8')
            df = pd.read_csv(io.StringIO(content))

            # describe()
            stats = df.describe()
            context['stats'] = {
                'columns': stats.columns.tolist(),
                'stat_labels': stats.index.tolist(),
                'stat_data': stats.values.tolist(),
            }

            # グラフ（hist）
            fig = df.hist(figsize=(10, 8))
            plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_base64 = base64.b64encode(buf.read()).decode('utf-8')
            context['graph'] = image_base64

        return self.render_to_response(context)
