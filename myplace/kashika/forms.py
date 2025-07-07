from django import forms

class CsvUploadForm(forms.Form):
    file = forms.FileField(
        label='ファイルを選択',  # このlabelはHTMLの<label>には反映されません
        widget=forms.ClearableFileInput(attrs={
            'class': 'custom-file-input',
            'id': 'exampleInputFile'
        })
    )
