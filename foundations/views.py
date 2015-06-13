# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms


class QuadraticForm(forms.Form):
    width_foundation = forms.FloatField(label="Ширина фундамента(м)")
    length_foundation = forms.FloatField(label="Длина фундамента (м)")
    depth_foundation = forms.FloatField(label="Глубина заложения (м)")
    width_bucket = forms.FloatField(label="Ширина подколонника (м)")
    length_bucket = forms.FloatField(label="Длина подколонника (м)")
    height_above_ground = forms.FloatField(label="Высота подколонника над землей (м)")
    vertical_force = forms.FloatField(label="Вертикальная нагрузка (т)")
    horizontal_force = forms.FloatField(label="Горизонтальная нагрузка (т)")
    moment = forms.FloatField(label="Момент (тм)")
    resistance_soil = forms.FloatField(label="Расчетное сопротивление основания фундамента (т/м2)")

    def clean(self):
        data = self.cleaned_data
        if data < 0:
            raise forms.ValidationError("значение не может быть меньше 0!")
        return data


# weight of the foundation
def weight_found(width_foundation, length_foundation, depth_foundation,
                 width_bucket, length_bucket, height_above_ground):
    weight = width_foundation*length_foundation*depth_foundation*2 +\
        width_bucket*length_bucket*height_above_ground*2.75
    return weight


def load_in_found(vertical_force, weight_found,
                  horizontal_force, moment, depth_foundation, height_above_ground):
    vertical_load = vertical_force + weight_found
    moment = moment + horizontal_force*(depth_foundation+height_above_ground)
    return vertical_load, moment


def geometry(width_foundation, length_foundation):
    square = width_foundation*length_foundation
    resistance_moment = width_foundation*length_foundation**2 / 6
    return square, resistance_moment


def eccentricity(load_in_found):
    eccentricity = load_in_found[1] / load_in_found[0]
    return eccentricity


def pressure(load_in_found, geometry, eccentricity, length_foundation, width_foundation):
    if eccentricity <= 0.25*length_foundation:
        if eccentricity < length_foundation/1.6:
            pressure_max = load_in_found[0]/geometry[0] + load_in_found[1]/geometry[1]
            pressure_min = load_in_found[0]/geometry[0] - load_in_found[1]/geometry[1]
            return '\n \n Эпюра давления под подошвой фундамента имеет трапецивидный вид.\
            Максимальное краевое давление pmax = %.2f; pmin = %.2f' % (pressure_max, pressure_min)
        elif eccentricity == length_foundation/1.6:
            pressure_max = load_in_found[0]/geometry[0] + load_in_found[1]/geometry[1]
            pressure_min = load_in_found[0]/geometry[0] - load_in_found[1]/geometry[1]
            return '\n \n Эпюра давления под подошвой фундамента имеет треугольный вид.\
            Максимальное краевое давление pmax = %.2f; pmin = %.2f' % (pressure_max, pressure_min)
        elif eccentricity > length_foundation/1.6:
            c0 = length_foundation/2 - eccentricity
            if c0 <= length_foundation:
                pressure_max = 2*load_in_found[0] / (3*width_foundation*c0)
                return '\n \n Эпюра давления под подошвой имеет треугольную форму (имеется отрыв фундамента.\
                Максимальное краевое давление pmax=%.2f.\n \
                Величина отрыва подошвы фундамента Со = %.2f' % (pressure_max, c0)
            else:
                return '\n \n '
    else:
        max_eccentricity = 0.25 * length_foundation
        return '\n \n Эксцентриситет = %.2f больше предельного значения\
        (чертверть длины фундамента). Увелитьте размеры фундаменты!' % max_eccentricity

def conclusion(pressure, resistance_soil):
    if len(pressure) == 3:
        pass


def foundation_results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            width_foundation = form.cleaned_data.get('width_foundation')
            length_foundation = form.cleaned_data.get('length_foundation')
            depth_foundation = form.cleaned_data.get('depth_foundation')
            width_bucket = form.cleaned_data.get('width_bucket')
            length_bucket = form.cleaned_data.get('length_bucket')
            height_above_ground = form.cleaned_data.get('height_above_ground')
            vertical_force = form.cleaned_data.get('vertical_force')
            horizontal_force = form.cleaned_data.get('horizontal_force')
            moment = form.cleaned_data.get('moment')
            resistance_soil = form.cleaned_data.get('resistance_soil')

            weight_foundations = weight_found(width_foundation, length_foundation,
                                 depth_foundation, width_bucket, length_bucket, height_above_ground)

            load_in_foundations = load_in_found(vertical_force, weight_found(width_foundation, length_foundation,
                                                depth_foundation, width_bucket, length_bucket, height_above_ground),
                                                horizontal_force, moment, depth_foundation, height_above_ground)

            geometry_foundations = geometry(width_foundation, length_foundation)

            eccentricity_foundations = eccentricity(load_in_foundations)

            pressure_foundations = pressure(load_in_foundations, geometry_foundations, eccentricity_foundations,
                                            length_foundation, width_foundation)

            return render(request, "foundation-result.html",
                          {'form': form, 'weight_foundations': weight_foundations,
                                         'load_in_foundations': load_in_foundations,
                                         'geometry_foundations': geometry_foundations,
                                         'eccentricity_foundations': eccentricity_foundations,})
        else:
            return render(request, "foundation-result.html", {'form': form})
    else:
        form = QuadraticForm()
        return render(request, "foundation-result.html", {'form': form})
