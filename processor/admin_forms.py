from django import forms

from processor.models import Client
from tenant_service.models import Patient


class PatientForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        required=True, queryset=Client.objects.exclude(schema_name="public")
    )
    exclude = []

    def __init__(self, *args, **kwargs):
        self.request = None
        super(PatientForm, self).__init__(*args, **kwargs)

    def save(self, commit=False):
        client = self.cleaned_data.pop("client")
        # if self.errors:
        #     raise ValueError(
        #         "The %s could not be %s because the data didn't validate." % (
        #             self.instance._meta.object_name,
        #             'created' if self.instance._state.adding else 'changed',
        #         )
        #     )
        # self.save_m2m = self._save_m2m
        # with tenant_context(client):
        #     if self.instance.pk:
        #         # TODO: untested
        #         Patient.objects.filter(pk=self.instance.pk).update(**self.cleaned_data)
        #     else:
        #         Patient.objects.create(**self.cleaned_data)
        #
        # return
        return super(PatientForm, self).save(commit=commit)

    class Meta:
        model = Patient
        fields = ["name"]
