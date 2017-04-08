from flask import (Flask, request, g, render_template, flash, redirect, url_for, abort)


import models
import forms

DEBBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '%'
app.secret_key = 'aldskfj32235adslfkjads!.aldsfjk'

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route('/')
def index():
    entries = models.Entry.select()
    return render_template('index.html', index=index, entries=entries)

@app.route('/detail_<title>')
def detail(title):
    entries = models.Entry.select()
    return render_template('detail.html', entries=entries, title=title)


@app.route('/new.html', methods=('GET', 'POST'))
def new():
    form = forms.EntryForm()
    if form.validate_on_submit():
        models.Entry.create(title=form.title.data.strip(),
                            date=form.date.data,
                            timeSpent=form.timeSpent.data.strip(),
                            whatILearned=form.whatILearned.data,
                            ResourcesToRemember=form.ResourcesToRemember.data)
        flash('Your entry has been Recorded, Good Job Today!', 'success')
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit(title):
    entry = models.Entry.select().where(models.Entry.title == title).get()
    form = forms.EntryForm(obj=entry)
    if request.method == 'POST':
        if form.validate_on_submit():
            entry.title = form.title.data
            entry.date = form.date.data
            entry.timeSpent = form.timeSpent.data
            entry.whatILearned = form.whatILearned.data
            entry.ResourcesToRemember = form.ResourcesToRemember.data
            entry.save()
            flash('Entry updated!', "success")
            return redirect(url_for('index'))
    return render_template('edit.html', title=title, entry=entry, form=form)


@app.route('/delete/<title>', methods=['GET', 'POST'])
def delete(title):
    entry = models.Entry.select().where(models.Entry.title == title).get()
    entry.delete_instance()
    return redirect(url_for('index'))
    return render_template('edit.html', title=title, entry=entry)


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBBUG, host=HOST, port=PORT)

