


@app.route("/resume")
def resume ():
    return render_template('resume.html')

@app.route("/about")
def about ():
    return render_template('about.html')

@app.route("/contact")
def contact ():
    return render_template('contact.html')
