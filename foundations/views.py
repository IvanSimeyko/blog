# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms


class QuadraticForm(forms.Form):
    b = forms.FloatField(label="Ширина фундамента(м),  B = ")
    l = forms.FloatField(label="Длина фундамента (м),  L = ")
    h = forms.FloatField(label="Глубина заложения (м),  h = ")
    x = forms.FloatField(label="Ширина подколонника (м),  x = ")
    y = forms.FloatField(label="Длина подколонника (м),  y = ")
    h1 = forms.FloatField(label="Высота подколонника над землей (м), h1 = ")
    N = forms.FloatField(label="Вертикальная нагрузка (т),  N = ")
    Q = forms.FloatField(label="Горизонтальная нагрузка (т),  Q = ")
    M = forms.FloatField(label="Момент (тм),  M = ")
    R = forms.FloatField(label="Расчетное сопротивление основания фундамента (т/м2),  R =")
    epurs = forms.ChoiceField(label="Допускаемая форма эпюры давления фундаментов",
                              choices=(('1', 'трапецевидная с pmin/pmax >= 0.25'),
                                      ('2', 'треугольная без отрыва подошвы'),
                                      ('3', 'треугольная с отрывом подошвы'),))

    def clean(self):
        data = self.cleaned_data
        if data < 0:
            raise forms.ValidationError("значение не может быть меньше 0!")
        return data


# weight of the foundation
def weight_found(b, l, h, x, y, h1):
    weight = b*l*h*2 + x*y*h1*2.75
    return weight


def load_in_found(N, Q, b, l, h, x, y, h1, M):
    vertical_load = N + weight_found(b, l, h, x, y, h1)
    moment = M + Q*(h+h1)
    return vertical_load, moment


def geometry(b, l):
    square = b*l
    resistance_moment = b*l**2 / 6
    return square, resistance_moment


def eccentricity(N, Q, b, l, h, x, y, h1, M):
    eccentricity = load_in_found(N, Q, b, l, h, x, y, h1, M)[1] / load_in_found(N, Q, b, l, h, x, y, h1, M)[0]
    return eccentricity


def pressure(N, Q, b, l, h, x, y, h1, M, R):
    if eccentricity(N, Q, b, l, h, x, y, h1, M) <= 0.25*l:
        if eccentricity(N, Q, b, l, h, x, y, h1, M) < l/6:
            pressure_max = load_in_found(N, Q, b, l, h, x, y, h1, M)[0]/geometry(b, l)[0] + \
                           load_in_found(N, Q, b, l, h, x, y, h1, M)[1]/geometry(b, l)[1]
            pressure_min = load_in_found(N, Q, b, l, h, x, y, h1, M)[0]/geometry(b, l)[0] - \
                           load_in_found(N, Q, b, l, h, x, y, h1, M)[1]/geometry(b, l)[1]
            pressure_soil = pressure_max / geometry(b, l)[0]
            if pressure_soil <= 1.2 * R:
                text = 'Эпюра давления под подошвой фундамента имеет трапецивидный вид. \n \
                       Максимальное краевое давление pmax = %.2f (т/м2); минимальное pmin = %.2f (т/м2)' \
                       % (pressure_max, pressure_min)
                return text
            else:
                return '\n \n Максимальное напряжение pmax = %.2f (т/м2) превышает допустимое Rmax = %.2f (т/м2).\
                Увеличьте размеры фундамента' % (pressure_max, 1.2*R)

        elif eccentricity(N, Q, b, l, h, x, y, h1, M) == l/6:
            pressure_max = load_in_found(N, Q, b, l, h, x, y, h1, M)[0]/geometry(b, l)[0] + \
                           load_in_found(N, Q, b, l, h, x, y, h1, M)[1]/geometry(b, l)[1]
            pressure_soil = pressure_max / geometry(b, l)[0]
            if pressure_soil <= 1.2 * R:
                return '\n \n Эпюра давления под подошвой фундамента имеет треугольный вид.\
                Максимальное краевое давление pmax = %.2f (т/м2); pmin = 0' % pressure_max
            else:
                return '\n \n Максимальное напряжение pmax = %.2f (т/м2) превышает допустимое Rmax = %.2f (т/м2).\
                Увеличьте размеры фундамента' % (pressure_max, 1.2*R)

        elif l/6 < eccentricity(N, Q, b, l, h, x, y, h1, M) < l/4:
            c0 = l/2 - eccentricity(N, Q, b, l, h, x, y, h1, M)
            gap_found = l-(3*c0)
            pressure_max = 2*load_in_found(N, Q, b, l, h, x, y, h1, M)[0] / (3*b*c0)
            pressure_soil = pressure_max / geometry(b, l)[0]
            if pressure_soil <= 1.2 * R:
                return '\n \n Эпюра давления под подошвой имеет треугольную форму (имеется отрыв фундамента.\
                       Максимальное краевое давление pmax=%.2f. (т/м2) \n \
                       Величина отрыва подошвы фундамента Со = %.2f' % (pressure_max, gap_found)
            else:
                return '\n \n Максимальное напряжение pmax = %.2f (т/м2) превышает допустимое Rmax = %.2f (т/м2).\
                Увеличьте размеры фундамента' % (pressure_max, 1.2*R)

    else:
        max_eccentricity = 0.25 * l
        return '\n \n Эксцентриситет = %.2f больше предельного значения\
        (%.2f). Увеличьте размеры фундаменты!' % (eccentricity(N, Q, b, l, h, x, y, h1, M), max_eccentricity)


def foundation_results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            b = form.cleaned_data.get('b')
            l = form.cleaned_data.get('l')
            h = form.cleaned_data.get('h')
            x = form.cleaned_data.get('x')
            y = form.cleaned_data.get('y')
            h1 = form.cleaned_data.get('h1')
            N = form.cleaned_data.get('N')
            Q = form.cleaned_data.get('Q')
            M = form.cleaned_data.get('M')
            R = form.cleaned_data.get('R')
            epurs = form.cleaned_data.get('epurs')

            weight_foundations = '\n \n \n Вес фундамента = %.2f (т)' % weight_found(b, l, h, x, y, h1)

            load_in_foundations = '\n \n \n Нагрузка на обрезе фундамента N = {} (т), M = {} (тм)' \
                                  .format(load_in_found(N, Q, b, l, h, x, y, h1, M)[0],
                                          load_in_found(N, Q, b, l, h, x, y, h1, M)[1])

            geometry_foundations = geometry(b, l)

            eccentricity_foundations = '\n \n \n Относительный эксцентриситет приложения нагружки %.2f'\
                                       % eccentricity(N, Q, b, l, h, x, y, h1, M)

            pressure_foundations = pressure(N, Q, b, l, h, x, y, h1, M, R)

            e = epurs
            return render(request, "foundation-result.html",
                          {'form': form, 'weight_foundations': weight_foundations,
                                         'load_in_foundations': load_in_foundations,
                                         'geometry_foundations': geometry_foundations,
                                         'eccentricity_foundations': eccentricity_foundations,
                                         'pressure_foundations': pressure_foundations,
                                         'e': e})
        else:
            return render(request, "foundation-result.html", {'form': form})
    else:
        form = QuadraticForm()
        return render(request, "foundation-result.html", {'form': form})
