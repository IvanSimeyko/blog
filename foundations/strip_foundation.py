# -*- coding: utf-8 -*-

from django import forms
from django.shortcuts import render


class StripFoundationForM(forms.Form):

    R = forms.FloatField(label='Расчетное сопротивления грунта', initial='т/м2')
    N = forms.FloatField(label='Нагрузка на фундамент', initial='т/м.пог')
    h = forms.FloatField(label='Высота ленточного фундамента', initial='м')

    def clean(self):
        data = self.cleaned_data
        if data < 0:
            raise forms.ValidationError("значение не может быть меньше 0!")
        return data


def width(R, N, h):
    width = N/(R-2.0*h)
    return 'Требуемая ширина подошвы = %.2f м.' % width


def strip_foundation(request):
    page_title = 'Определение ширины ленточного фундамента'
    if request.GET:
        form = StripFoundationForM(request.GET)
        if form.is_valid():
            R = form.cleaned_data.get('R')
            N = form.cleaned_data.get('N')
            h = form.cleaned_data.get('h')
            result = width(R, N, h)
            return render(request, "foundations/strip-result.html", {
                'form': form,
                'result': result,
                'page_title': page_title,
            }
            )
        else:
            return render(request, "foundations/strip-result.html", {
                'form': form,
                'page_title': page_title,
            }
            )
    else:
        form = StripFoundationForM()
        return render(request, "foundations/strip-result.html", {
            'form': form,
            'page_title': page_title,
        }
        )