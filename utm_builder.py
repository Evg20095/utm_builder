from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!!!!!!!!!!'

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

# class first_form(FlaskForm):
#     radio_sourse = RadioField('Label', choices=[('value','yandex'),('value_two','google')])
#     domain = StringField('Введите Адрес целевой страницы: (не забудьте http://)') 
#     sourse = StringField('Источник кампании:') 
#     medium = StringField('Тип трафика:') 
#     campaign = StringField('Название кампании:')
#     content = StringField('Идентификатор объявления:')
#     term = StringField('Ключевое слово:')
#     utm_ref = StringField('Ваша ссылка:')


    


# @app.route('/utm_builder2', methods=('GET', 'POST'))
# def submit_first():
#     form1 = first_form()
#     if form1.validate_on_submit() and form1.radio_sourse.data == 'value' and form1.sourse.data == None:

#         form1.sourse.data = 'google'
#         form1.medium.data = 'cpc'
#         form1.campaign.data = '{network}'
#         form1.content.data = '{creative}'
#         form1.term.data = '{keyword}'

#         utm_sourse = 'utm_sourse=' + form1.sourse.data
#         utm_medium = '&utm_medium=' + form1.medium.data
#         utm_campaign = '&utm_campaign=' + form1.campaign.data
#         utm_content = '&utm_content=' + form1.content.data
#         utm_term = '&utm_term=' + form1.term.data

#         form1.utm_ref.data = form1.domain.data + '/?' + utm_sourse + utm_medium + utm_campaign + utm_content + utm_term

#         # print(utm_adres)
#         # print(form.domain)
        

#         return render_template('first_form.html', form=form1)

#     # if form1.validate_on_submit() and form1.radio_sourse.data == 'value':

#     #     print (form1.radio_sourse.data)
#     #     #return redirect('/utm_bulder2')
#     #     return 'yandex'

#     return render_template('first_form.html', form=form1)



class second_form(FlaskForm):
    domain = StringField(label = 'Введите Адрес целевой страницы: (не забудьте https://)') 
    radio_source = RadioField('Label', choices=[('ya','yandex'),('goo','google')])
    source = StringField('Источник кампании:')
    medium = StringField('Тип трафика:') 
    campaign = StringField('Название кампании:')
    content = StringField('Идентификатор объявления:')
    term = StringField('Ключевое слово:') 
    utm_ref = StringField('Ваша ссылка:')
    submit = SubmitField('Сформировать стандартные значения utm')
    submit2 = SubmitField('Создать utm')

@app.route('/utm_creat', methods=('GET', 'POST'))
def submit_second():
    form2 = second_form()
    if form2.validate_on_submit():
        if form2.submit.data:
            if form2.radio_source.data == 'ya':
                form2.source.data = 'yandex'
                form2.medium.data = 'cpc'
                form2.campaign.data = '{campaign_id}'
                form2.content.data = '{ad_id}_{source}'
                form2.term.data = '{keyword}'
                return render_template('second_form.html', form=form2)
            
            if form2.radio_source.data == 'goo':
                form2.source.data = 'google'
                form2.medium.data = 'cpc'
                form2.campaign.data = '{network}'
                form2.content.data = '{creative}'
                form2.term.data = '{keyword}'
                return render_template('second_form.html', form=form2)
                
        elif form2.submit2.data:
            utm_source = 'utm_sourse=' + form2.source.data
            utm_medium = '&utm_medium=' + form2.medium.data
            utm_campaign = '&utm_campaign=' + form2.campaign.data
            utm_content = '&utm_content=' + form2.content.data
            utm_term = '&utm_term=' + form2.term.data
            form2.utm_ref.data = form2.domain.data + '/?' + utm_source + utm_medium + utm_campaign + utm_content + utm_term
            return render_template('second_form.html', form=form2)
        return render_template('second_form.html', form=form2)
    return render_template('second_form.html', form=form2)


