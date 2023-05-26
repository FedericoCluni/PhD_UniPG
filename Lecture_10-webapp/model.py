from wtforms import Form, FloatField, validators

def check_float(form, field):
    v = field.data
    try:
        v = float(v)
    except TypeError:
        raise validators.ValidationError('Must be a number!')

def check_x2(form, field):
    x2 = field.data
    x1 = form.x1.data
    if x2 <= x1:
        raise validators.ValidationError('Must be \(x_2 > x_1\)')
    
class InputForm(Form):
    m = FloatField(
        label='slope', default=1.0, description='m', validators=[check_float])
    b = FloatField(
        label='intercept', default=0, description='b')
    x1 = FloatField(
        label='left bound', default=0., description="x_1")
    x2 = FloatField(
        label='right bound', default=1., description="x_2", validators=[check_x2])
